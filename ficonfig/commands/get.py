import sys

from .main import command, argument
from ..utils import normalize_key

@command(
    argument('-n', '--no-newline', action='store_true', help="don't print trailing newline"),
    argument('key', type=normalize_key, nargs=1),
    argument('default', nargs='?', default=None, help="default value if `key` isn't set"),
    name='get',
    help='lookup a single key',
)
def get_(args, config):

    pattern = '{%s}' % args.key[0]
    try:
        value = pattern.format(**config)
    except KeyError:
        raise
        value = None

    value = value if value is not None else args.default

    if value is None:
        return 1

    sys.stdout.write(str(value) + ('' if args.no_newline else '\n'))
