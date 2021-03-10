import unittest
from twitter.twitter_util import *


class TwitterUtilTest(unittest.TestCase):

    def test_get_direct_messages(self):
        m = get_direct_messages()

        self.assertIsNotNone(m)

