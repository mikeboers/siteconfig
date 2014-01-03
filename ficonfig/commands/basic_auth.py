import sys

from .main import command, argument
from ..utils import normalize_key

@command(
    argument('base', type=normalize_key, nargs=1),
    name='basic-auth',
    help='construct user:password from a base',
)
def host_string(args, config):

    try:
        value = '%s:%s' % (
            config[args.base[0] + '_USER'],
            config[args.base[0] + '_PASSWORD'],
        )
    except KeyError as e:
        print >> sys.stderr, 'missing', e.args[0]
        return 1

    sys.stdout.write(value + args.endl)
