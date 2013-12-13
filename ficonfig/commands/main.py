import argparse

from .. import config


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help')


def argument(*args, **kwargs):
    return args, kwargs


def command(*args, **kwargs):
    def _decorator(func):

        command_parser = subparsers.add_parser(
            kwargs.pop('name', func.__name__),
            help=kwargs.pop('help', None),
        )
        for arg_args, arg_kwargs in args:
            command_parser.add_argument(*arg_args, **arg_kwargs)

        command_parser.set_defaults(func=func)

        return func

    return _decorator


# Register the commands.
from . import get
from . import list as list_
from . import host_string


def main():
    args = parser.parse_args()
    exit(args.func(args, config) or 0)
