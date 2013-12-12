from .main import command, argument

@command(
    argument('name', nargs=1),
    name='get',
    help='lookup a single key',
)
def get_(args, config):
    value = config.get(args.name[0])
    if value is not None:
        print value
    else:
        exit(1)
