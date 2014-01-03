import sys

from .main import command, argument


@command(
    argument('expr', nargs='+'),
    name='eval',
    help='lookup a single key',
)
def get_(args, config):
    value = eval(' '.join(args.expr), {}, config)
    if value is None:
        return 1
    sys.stdout.write(str(value) + args.endl)
