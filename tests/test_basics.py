from common import *


class TestBasics(TestCase):

    def test_example_loaded_python(self):
        for name in 'A', 'B', 'C':
            self.assertTrue(config.get('LOADED_%s' % name))

    def test_example_loaded_shell(self):
        for name in 'A', 'B', 'C':
            self.assertEqual('True', run('ficonfig get LOADED_%s' % name).strip())

