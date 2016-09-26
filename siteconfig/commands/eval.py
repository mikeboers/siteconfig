import sys

from .main import command, argument


@command(
    argument('expr', nargs='+'),
    name='eval',
    help='lookup a single key',
)
def eval_(args, config):

    globals_ = dict(config)
    locals_ = {'config': config}
    value = eval(' '.join(args.expr), globals_, locals_)

    if value is None:
        return 1
    sys.stdout.write(str(value) + args.endl)

