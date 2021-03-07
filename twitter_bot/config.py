import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def get_twitter_api_key():
    return os.environ.get("TWITTER_API_KEY", "")


def get_twitter_api_secret_key():
    return os.environ.get("TWITTER_API_SECRET_KEY", "")


def get_twitter_access_token():
    return os.environ.get("TWITTER_ACCESS_TOKEN", "")


def get_twitter_access_token_secret():
    return os.environ.get("TWITTER_ACCESS_TOKEN_SECRET", "")



