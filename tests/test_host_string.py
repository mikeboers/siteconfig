from common import *


class TestHostString(TestCase):

    def test_aaa(self):
        self.assertEqual('alice:apass@a.com:12345', run('ficonfig --host-string AAA').strip())
        self.assertEqual('alice@a.com:12345', run('ficonfig --host-string --no-password AAA').strip())
        self.assertEqual('alice@a.com', run('ficonfig --host-string --no-password --no-port AAA').strip())

