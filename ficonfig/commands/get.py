from .main import command, argument

@command(
    argument('name', nargs=1),
    argument('default', nargs='?', default=None),
    name='get',
    help='lookup a single key',
)
def get_(args, config):
    value = config.get(args.name[0])
    if value is not None:
        print value
    elif args.default is not None:
        print args.default
    else:
        exit(1)
