from common import *


class TestBasicAuth(TestCase):

    def test_aaa(self):
        self.assertEqual('alice:apass', run('siteconfig --basic-auth AAA').strip())

