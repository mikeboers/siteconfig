import sys

from .main import command, argument, format


@command(
    argument('key', nargs='*'),
    argument('-d', '--default', default=None, help="default value if `key` isn't set"),
    name='get',
    help='lookup a single key',
)
def get_(args, config):

    values = []

    for key in args.key:
        value = config.get(key)
        value = value if value is not None else args.default
        if value is None:
            return 1
        values.append(value)

    formatted = format(args, values, config)
    if formatted is not None:
        sys.stdout.write(formatted + args.endl)
    elif values:
        sys.stdout.write(' '.join(str(v) for v in values) + args.endl)
    else:
        return 1
