import tweepy
import logging

from config import *

auth = tweepy.OAuthHandler(get_twitter_api_key(), get_twitter_api_secret_key())
auth.set_access_token(get_twitter_access_token(), get_twitter_access_token_secret())

api = tweepy.API(auth)


def get_api():
    return api


def extract_url(message):
    message_data = message.message_create["message_data"]
    list_urls = message_data["entities"]["urls"]

    if len(list_urls) > 0:
        url = list_urls[0]['expanded_url']
    else:
        url = None

    return url


def get_sender_id(message):
    return message.message_create["sender_id"]


def find_my_followers():
    followers = get_api().followers()

    logging.info(f'Followers {followers}')

    return followers


def is_my_follower(user_id):
    ret = False

    followers = find_my_followers()

    for user in followers:
        if user_id == user.id_str:
            ret = True
            break

    return ret


def delete_direct_message(direct_message):
    if direct_message is not None:
        get_api().destroy_direct_message(direct_message.id)


def send_direct_message(sender_id, text):
    get_api().send_direct_message(sender_id, text)


def get_direct_messages():
    messages = get_api().list_direct_messages(count=5)

    return messages

def get_tweet_by_id(id):
    return get_api().get_status(id=id)





