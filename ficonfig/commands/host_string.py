import sys

from .main import command, argument

@command(
    argument('base', nargs=1),
    name='host-string',
)
def host_string(args, config):

    base = args.base[0].rstrip('_') + '_'

    # If it is set directly, use that.
    full = config.get(base + 'HOSTSTRING')
    if full is not None:
        print full
        return

    try:
        host = config[base + 'HOST']
    except KeyError as e:
        print >> sys.stderr, 'missing', e.args[0]
        exit(1)

    port = config.get(base + 'PORT')
    if port is not None:
        host = '%s:%s' % (host, port)

    user = config.get(base + 'USER')
    if user is not None:
        host = '%s@%s' % (user, host)

    print host
    
