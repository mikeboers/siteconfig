import argparse
import collections
import string
import sys

from .. import config
from ..utils import normalize_key


class TransformedView(collections.Mapping):

    def __init__(self, base_map, key_func):
        self.base_map = base_map
        self.key_func = key_func

    def __getitem__(self, key):
        return self.base_map[self.key_func(key)]

    def __iter__(self):
        return iter(self.base_map)

    def __len__(self):
        return len(self.base_map)

    def __getattr__(self, name):
        return getattr(self.base_map, name)


parser = argparse.ArgumentParser()

actions = parser.add_argument_group('actions')
actions_mutex = actions.add_mutually_exclusive_group()

formats = parser.add_argument_group('formats')
formats_mutex = formats.add_mutually_exclusive_group()
formats_mutex.add_argument('-f', '--format')
formats_mutex.add_argument('--printf')

parser.add_argument('-n', '--no-newline', action='store_const', dest='endl', default='\n', const='', help="don't print trailing newline")
parser.add_argument('-x', '--raw-key', action='store_true', help="don't normalize keys")
parser.add_argument('-p', '--prefix', help="key prefix")



def argument(*args, **kwargs):
    return args, kwargs


_commands = {}
def command(*args, **kwargs):
    def _decorator(func):
        name = kwargs.pop('name', func.__name__)
        _commands[name] = (func, args)
        actions_mutex.add_argument(
            '--' + name,
            help=kwargs.pop('help', None),
            action='store_const',
            dest='action',
            const=name,
        )
        return func

    return _decorator


def format(opts, args, kwargs):

    if opts.printf:
        if args:
            return opts.printf % args
        else:
            return opts.printf % kwargs

    if opts.format:
        if args:
            return opts.format.format(*args)
        else:
            return string.Formatter().vformat(opts.format, (), kwargs)


# Register the commands.
import ficonfig.commands.basic_auth
import ficonfig.commands.eval
import ficonfig.commands.get
import ficonfig.commands.host_string
import ficonfig.commands.list
import ficonfig.commands.set
import ficonfig.commands.sync



def main():

    opts, leftovers = parser.parse_known_args()
    action_name = opts.action or ('get' if leftovers else None)
    action_spec = _commands.get(action_name)

    if not action_spec:
        parser.print_usage()
        exit(1)

    func, func_args = action_spec
    subparser = argparse.ArgumentParser(add_help=False, parents=[parser])
    for arg_args, arg_kwargs in func_args:
        subparser.add_argument(*arg_args, **arg_kwargs)

    opts = subparser.parse_args()

    config_view = config

    if not opts.raw_key:
        config_view = TransformedView(config_view, normalize_key)
    if opts.prefix:
        config_view = TransformedView(config_view, lambda k: opts.prefix + k)

    exit(func(opts, config_view) or 0)



