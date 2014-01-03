from common import *


class TestBasics(TestCase):

    def test_example_loaded_python(self):
        for name in 'A', 'B', 'C':
            self.assertTrue(config.get('LOADED_%s' % name))

    def test_example_loaded_shell(self):
        for name in 'A', 'B', 'C':
            self.assertEqual('True', run('ficonfig get LOADED_%s' % name).strip())

    def test_example_loaded_shell_case(self):
        self.assertEqual('True', run('ficonfig get loaded.a').strip())

    def test_shell_get_default(self):
        self.assertEqual('default', run('ficonfig get DOES_NOT_EXIST default').strip())

    def test_shell_get_eval(self):
        self.assertEqual('COM', run('''ficonfig get --eval 'ALICE_HOST.split(".")[-1].upper()' ''').strip())
