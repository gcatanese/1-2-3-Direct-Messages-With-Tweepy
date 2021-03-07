import threading
import logging

from twitter.twitter_util import extract_url, send_direct_message, get_sender_id, delete_direct_message


class MessageWorker():

    def __init__(self, message):
        self.message = message

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        logging.info(f'run MessageWorker')

        url = extract_url(self.message)
        sender_id = get_sender_id(self.message)

        try:

            reply = send_direct_message(sender_id, "Hello from Beppe")
        except Exception:
            logging.info(f'Error')

        delete_direct_message(reply)


