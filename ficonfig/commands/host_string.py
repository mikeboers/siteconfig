import sys

from .main import command, argument
from ..utils import normalize_key

@command(
    argument('base', type=normalize_key, nargs=1),
    argument('-n', '--no-newline', action='store_true', help="don't print trailing newline"),
    argument('--no-user', action='store_true'),
    argument('--no-password', action='store_true'),
    argument('--no-port', action='store_true'),
    name='host-string',
    help='construct user@host:port from a base',
)
def host_string(args, config):

    try:
        value = config.host_string(
            args.base[0],
            user=not args.no_user,
            password=not args.no_password,
            port=not args.no_port,
        )
    except KeyError as e:
        print >> sys.stderr, 'missing', e.args[0]
        return 1

    sys.stdout.write(value + ('' if args.no_newline else '\n'))
