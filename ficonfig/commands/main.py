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
import ficonfig.commands.basic_auth
import ficonfig.commands.get
import ficonfig.commands.host_string
import ficonfig.commands.list


def main():
    args = parser.parse_args()
    exit(args.func(args, config) or 0)
