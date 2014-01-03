import socket
import sys
from subprocess import call


from .main import command, argument
from ..utils import normalize_key

@command(
    argument('-n', '--dry-run'),
    name='sync',
    help='transfer to the other host',
)
def get_(args, config):

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com", 80))
    local_ip = s.getsockname()[0]
    s.close()

    if local_ip.split('.')[-1] != '221':
        print 'This is not the first machine.'
        return 1

    remote_ip = local_ip[:-1] + '2'

    command = ['rsync', '-avx', '~offload/ficonfig/', 'offload@%s:ficonfig/' % remote_ip]
    print ' '.join(command)

    if args.dry_run:
        return

    return call(command)
