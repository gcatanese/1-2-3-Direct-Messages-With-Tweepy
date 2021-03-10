import unittest
from twitter.twitter_rest import *


class TwitterRestTest(unittest.TestCase):

    def test_oauth2_bearer_token(self):
        m = obtain_oauth2_bearer_token()
        self.assertIsNotNone(m)

    def test_create_welcome_message(self):
        token = obtain_oauth2_bearer_token()

        r = create_welcome_message('msg1', 'Welcome here', token)
        self.assertIsNotNone(r)
