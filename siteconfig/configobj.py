import ast
import errno
import json
import logging
import os
import traceback
import warnings


log = logging.getLogger('siteconfig')


DEFAULT_ENVVAR_NAME = 'SITECONFIG'


class Config(dict):

    @classmethod
    def from_environ(cls, envvar_name=DEFAULT_ENVVAR_NAME):
        self = cls()
        self.envvar_name = envvar_name
        self.scan_envvar()
        self.process()
        self.import_environ()
        return self

    def __init__(self):
        self.dir_paths = []
        self.file_paths = []
        self.processed = set()

    def scan_envvar(self, envvar_name=None):
        path = os.environ.get(envvar_name or self.envvar_name)
        path = default if path is None else path
        if path is not None:
            log.log(5, 'reading from %s' % path)
            self.dir_paths.extend(path.split(':'))

    def import_environ(self, prefix=None):

        if prefix is None:
            prefix = self.envvar_name

        for k, v in os.environ.iteritems():

            if not k.isupper():
                continue
            if not k.startswith(prefix):
                continue
            
            k = k[len(prefix):].lstrip('_')
            if not k:
                continue

            try:
                v = ast.literal_eval(v)
            except (ValueError, SyntaxError):
                pass
            
            self[k] = v

    def process(self):

        new_file_paths = []
        for dir_path in self.dir_paths:

            # Only process this once.
            if dir_path in self.processed:
                continue
            self.processed.add(dir_path)

            try:
                file_names = os.listdir(dir_path)
            except OSError as e:
                if e.errno == errno.ENOENT:
                    continue
                else:
                    raise

            for file_name in os.listdir(dir_path):
                new_file_paths.append(os.path.join(dir_path, file_name))

        new_file_paths.sort(key=os.path.basename)
        self.file_paths.extend(new_file_paths)

        namespace = self.copy()

        for file_path in new_file_paths:

            # Only process this once.
            if file_path in self.processed:
                continue
            self.processed.add(file_path)

            log.log(5, 'processing %s' % file_path)

            ext = os.path.splitext(file_path)[1]
            if ext == '.py':
                try:
                    helpers = {
                        'config': namespace,
                        'get': namespace.get,
                        'setdefault': namespace.setdefault,
                    }
                    execfile(file_path, helpers, namespace)
                except Exception as e:
                    warnings.warn('error in Python config:\n%s' % traceback.format_exc())

            elif ext in ('.js', '.json'):
                try:
                    namespace.update(json.load(open(file_path)))
                except ValueError as e:
                    warnings.warn('invalid JSON config %s: %s' % (file_path, e))

            namespace = dict((k, v) for k, v in namespace.iteritems() if k.isupper())

        self.update(namespace)

    def get_bool(self, key, default=None, strict=True):
        
        value = self.get(key)
        if value is None:
            return default

        if isinstance(value, bool):
            return value

        if isinstance(value, int) and value in (0, 1):
            return bool(value)

        if isinstance(value, basestring):
            adapted = {
                'true': True,
                't': True,
                'yes': True,
                'y': True,
                'false': False,
                'f': False,
                'no': False,
                'n': False,
                '': False,
            }.get(value.lower())
            if adapted is not None:
                return adapted

        if strict:
            raise ValueError('non-obvious boolean value', value)
        else:
            return bool(value)

    def host_string(self, base_key, user=True, password=True, port=True):

        base = base_key.rstrip('_') + '_'

        # If it is set directly, use that.
        full = self.get(base + 'HOSTSTRING')
        if full is not None:
            return full

        # Let this KeyError raise through.
        host = self[base + 'HOST']

        if port:
            port = self.get(base + 'PORT')
            if port is not None:
                host = '%s:%s' % (host, port)

        if user:
            user = self.get(base + 'USER')
            if user is not None:
                if password:
                    password = self.get(base + 'PASSWORD')
                    if password is not None:
                        user = '%s:%s' % (user, password)
                host = '%s@%s' % (user, host)

        return host


