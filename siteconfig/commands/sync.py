import socket
import sys
from subprocess import call


from .main import command, argument
from ..utils import normalize_key

@command(
    argument('--dry-run', action='store_true'),
    name='sync',
    help='transfer to the other host',
)
def get_(args, config):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    local_ip = sock.getsockname()[0]
    sock.close()

    if local_ip.split('.')[-1] != '221':
        print 'Please use from the primary server.'
        return 1

    remote_ip = local_ip[:-1] + '2'

    command = ['rsync', '-avx', '/home/offload/ficonfig/', 'offload@%s:ficonfig/' % remote_ip]
    print ' '.join(command)

    if args.dry_run:
        return

    return call(command)
