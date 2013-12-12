from .main import command, argument

@command(
    argument('-s', '--shell', action='store_true', help='format for a shell'),
    argument('-p', '--prefix', default='FICONFIG_', help='prefix for shell variables'),
    name='list',
    help='list all key-value pairs',
)
def list_(args, config):

    for k, v in sorted(config.iteritems()):
        if args.shell:
            print '%s%s="%s"' % (args.prefix, k, str(v).replace('"',  '\\"'))
        else:
            print '%s = %r' % (k, v)

