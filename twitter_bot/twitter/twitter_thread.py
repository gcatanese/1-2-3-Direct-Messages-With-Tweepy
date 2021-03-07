import threading
import time

from service.message_worker import MessageWorker
from twitter.twitter_util import *


class TwitterThread():

    def start(self):

        self.interval = 60

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        """ Method that runs forever """
        while True:
            try:

                messages = get_direct_messages()

                for message in reversed(messages):

                    try:

                        sender_id = get_sender_id(message)
                        logging.debug(f'DM from {sender_id}')

                        delete_direct_message(message)

                        MessageWorker(message)

                    except Exception as e:
                        logging.exception(e)

            except Exception as e:
                logging.exception(e)

            time.sleep(self.interval)
