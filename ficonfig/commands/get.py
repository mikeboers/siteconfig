import sys

from .main import command, argument
from ..utils import normalize_key

@command(
    argument('-n', '--no-newline', action='store_true', help="don't print trailing newline"),
    argument('-e', '--eval', action='store_true', help="eval as a Python expression"),
    argument('key', nargs=1),
    argument('default', nargs='?', default=None, help="default value if `key` isn't set"),
    name='get',
    help='lookup a single key',
)
def get_(args, config):

    if args.eval:
        value = eval(args.key[0], config)

    else:
        key = normalize_key(args.key[0])
        pattern = '{%s}' % key
        try:
            value = pattern.format(**config)
        except KeyError:
            value = None
        value = value if value is not None else args.default

    if value is None:
        return 1

    sys.stdout.write(str(value) + ('' if args.no_newline else '\n'))
