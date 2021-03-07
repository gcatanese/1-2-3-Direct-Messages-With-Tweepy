import unittest
import json
from tweepy import DirectMessage
from twitter.twitter_util import *


class TwitterUtilTest(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger().setLevel(logging.DEBUG)

    def test_get_direct_messages(self):
        m = get_direct_messages()
        print(m)
        # print(m[0].message_create["message_data"]["text"])
        # print(m[1].message_create["message_data"]["text"])

        self.assertIsNotNone(m)

    def test_send_direct_messages(self):

        m = send_direct_message("1163046315179294721", "Hoi hoi")
        print(m)

    def test_find_my_followers(self):

        followers = find_my_followers()
        print(followers)
        print(followers[0].name)
        print(followers[0].status.created_at)

        self.assertTrue(followers)

    def test_is_my_follower(self):

        self.assertTrue(is_my_follower('perosa_bots'))

    def test_get_tweet_by_id(self):

        tweet = get_tweet_by_id(1314302103976845344)
        self.assertIsNotNone(tweet)

    def test_cursor_my_followers(self):
        api = tweepy.API(auth)
        for follower in tweepy.Cursor(api.followers).items():
            print(follower.name)

