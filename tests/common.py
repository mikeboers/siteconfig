import os
from unittest import TestCase


from ficonfig import config

config.dir_paths.append(os.path.abspath(os.path.join(__file__, '..', 'example_config')))
config.process()


