import ast
import os
import sys

from .main import command, argument, format


@command(
    argument('--file', default='zzz_config.py'),
    argument('-e', dest='eval', action='store_true', help='eval the value'),
    argument('-r', '--raw', action='store_true', help='don\t repr the value'),
    argument('key'),
    argument('value'),
    name='set',
    help='set a key-value pair',
)
def set(args, config):

    if not os.path.isabs(args.file) and len(config.dir_paths) != 1:
        print >> sys.stderr, 'ficonfig: config from multiple directories; specify absolute --file'
        exit(1)

    value = args.value
    if args.eval:
        value = eval(value, {})

    path = os.path.join(config.dir_paths[0], args.file)
    with open(path, 'ab') as fh:
        fh.write('%s = %s\n' % (
            args.key.upper(),
            value if args.raw else repr(value),
        ))
