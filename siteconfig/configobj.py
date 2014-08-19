import errno
import json
import logging
import os
import traceback
import warnings


log = logging.getLogger('ficonfig')


class Config(dict):

    @classmethod
    def from_environ(cls, *args, **kwargs):
        self = cls()
        self.scan_envvar(*args, **kwargs)
        self.process()
        self.import_environ()
        return self

    def __init__(self):
        self.dir_paths = []
        self.file_paths = []
        self.processed = set()

    def scan_envvar(self, var_name='FICONFIG', default=None):

        path = os.environ.get(var_name, default)
        if path is None:
            fi_tools = os.environ.get("FI_TOOLS")

             # Really fallback here.
            if fi_tools is None:
                log.warning('FI_TOOLS is not set')
                fi_tools = os.path.abspath(os.path.join(__file__, '..', '..', '..'))

            path = os.path.join(os.path.dirname(fi_tools), 'ficonfig')

        log.log(5, 'reading from %s' % path)
        self.dir_paths.extend(path.split(':'))

    def import_environ(self, prefix='FICONFIG_'):
        for k, v in os.environ.iteritems():
            if k.startswith(prefix) and k.isupper():
                self[k[len(prefix):]] = v

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

        namespace = {}
        for file_path in new_file_paths:

            # Only process this once.
            if file_path in self.processed:
                continue
            self.processed.add(file_path)

            log.log(5, 'processing %s' % file_path)

            ext = os.path.splitext(file_path)[1]
            if ext == '.py':
                try:
                    execfile(file_path, namespace)
                except Exception as e:
                    warnings.warn('error in Python config:\n%s' % traceback.format_exc())
            elif ext in ('.js', '.json'):
                try:
                    namespace.update(json.load(open(file_path)))
                except ValueError as e:
                    warnings.warn('invalid JSON config %s: %s' % (file_path, e))

            namespace = dict((k, v) for k, v in namespace.iteritems() if k.isupper())

        self.update(namespace)

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


