import sys
from .main import command, argument

@command(
    argument('-n', '--no-newline', action='store_true', help="don't print trailing newline"),
    argument('key', type=str.upper, nargs=1),
    argument('default', nargs='?', default=None, help="default value if `key` isn't set"),
    name='get',
    help='lookup a single key',
)
def get_(args, config):
    
    value = config.get(args.key[0])
    value = value if value is not None else args.default

    if value is None:
        return 1

    sys.stdout.write(str(value) + ('' if args.no_newline else '\n'))
