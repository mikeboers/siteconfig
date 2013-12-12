from common import *


class TestHostString(TestCase):

    def test_aaa(self):
        self.assertEqual('alice@a.com:12345', run('ficonfig host-string AAA').strip())

