import tweepy

from config import *

auth = tweepy.OAuthHandler(get_twitter_api_key(), get_twitter_api_secret_key())
auth.set_access_token(get_twitter_access_token(), get_twitter_access_token_secret())

api = tweepy.API(auth)


def get_api():
    return api


def get_sender_id(message):
    return message.message_create["sender_id"]


def delete_direct_message(direct_message):
    if direct_message is not None:
        get_api().destroy_direct_message(direct_message.id)


def send_direct_message(sender_id, text):
    get_api().send_direct_message(recipient_id=sender_id, text=text)


def send_direct_message_with_media(sender_id, text, attachment_media_id):
    get_api().send_direct_message(recipient_id=sender_id, text=text, attachment_type='media', attachment_media_id=attachment_media_id)


def get_direct_messages():
    messages = get_api().list_direct_messages(count=5)

    return messages


def get_tweet_by_id(id):
    return get_api().get_status(id=id)


def upload_media(media):
    return get_api().media_upload(filename=media)






