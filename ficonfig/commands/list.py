from .main import command, argument
from ..utils import shell_quote

@command(
    argument('-s', '--shell', action='store_true', help='format for a shell'),
    name='list',
    help='list all key-value pairs',
)
def list_(args, config):

    for k, v in sorted(config.iteritems()):
        if args.shell:
            print '%s%s=%s' % (args.prefix if args.prefix is not None else 'FICONFIG_', k, shell_quote(v))
        else:
            print '%s = %r' % (k, v)

