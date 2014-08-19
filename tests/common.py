import os
from subprocess import check_output
from unittest import TestCase


from siteconfig import config

example_path = os.path.abspath(os.path.join(__file__, '..', 'example_config'))

# For subprocesses.
os.environ['FICONFIG'] = example_path

# For this process.
config.dir_paths.append(example_path)
config.process()


def run(command, env={}):
    environ = os.environ.copy()
    environ.update(env)
    return check_output(command, shell=True, env=environ)

