import requests
from config import *

OAUTH2_TOKEN_END_POINT = 'https://api.twitter.com/oauth2/token?grant_type=client_credentials'

WELCOME_MESSAGE_END_POINT = 'https://api.twitter.com/1.1/direct_messages/welcome_messages/new.json'


def obtain_oauth2_bearer_token():
    username = get_twitter_api_key()
    password = get_twitter_api_secret_key()

    r = requests.post(OAUTH2_TOKEN_END_POINT, auth=(username, password))

    token = r.json()["access_token"]

    return token


def create_welcome_message(name, msg, token):
    headers = {'Content-type': 'application/json', 'Authorization': f'Bearer {token}'}
    data = get_welcome_message_payload(name, msg)

    r = requests.post(WELCOME_MESSAGE_END_POINT, json=data, headers=headers)

    print(r.text)


def get_welcome_message_payload(name, msg):
    data = {
        'welcome_message': {
            'name': name,
            'message_data': {
                'text': msg
            }
        }
    }
    return data
