from common import *


class TestBasics(TestCase):

    def test_example_loaded_python(self):
        for name in 'A', 'B', 'C':
            self.assertTrue(config.get('LOADED_%s' % name))

    def test_example_loaded_shell(self):
        for name in 'A', 'B', 'C':
            self.assertEqual('True', run('ficonfig LOADED_%s' % name).strip())
            self.assertEqual('True', run('siteconfig LOADED_%s' % name).strip())

    def test_example_loaded_shell_case(self):
        self.assertEqual('True', run('siteconfig loaded.a').strip())

    def test_shell_get_default(self):
        self.assertEqual('fallback', run('siteconfig --default fallback DOES_NOT_EXIST').strip())

    def test_shell_get_eval(self):
        self.assertEqual('COM', run('''siteconfig --eval 'ALICE_HOST.split(".")[-1].upper()' ''').strip())

    def test_shell_get_pattern(self):
        self.assertEqual('alice@alice.com', run('''siteconfig -p alice. -f '{}@{}' user host''').strip())

    def test_shell_get_format(self):
        self.assertEqual('alice@alice.com', run('''siteconfig --get -p alice. -f '{user}@{host}' ''').strip())