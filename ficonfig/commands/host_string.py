import sys

from .main import command, argument

@command(
    argument('base', nargs=1),
    argument('--no-user', action='store_true'),
    argument('--no-password', action='store_true'),
    argument('--no-port', action='store_true'),
    name='host-string',
    help='construct user@host:port from a base',
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

    if not args.no_port:
        port = config.get(base + 'PORT')
        if port is not None:
            host = '%s:%s' % (host, port)

    if not args.no_user:
        user = config.get(base + 'USER')
        if user is not None:
            if not args.no_password:
                password = config.get(base + 'PASSWORD')
                if password is not None:
                    user = '%s:%s' % (user, password)
            host = '%s@%s' % (user, host)

    print host

