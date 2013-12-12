from common import *


class TestBasics(TestCase):

    def test_all_loaded(self):
        for name in 'A', 'B', 'B':
            self.assertTrue(config.get('LOADED_%s' % name))
    

