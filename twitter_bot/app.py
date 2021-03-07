import logging, os

from twitter.twitter_thread import TwitterThread


def create_app():
    try:
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
        logging.info(f'Starting up..')

        TwitterThread().start()

        return web_app

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    web_app = create_app()
