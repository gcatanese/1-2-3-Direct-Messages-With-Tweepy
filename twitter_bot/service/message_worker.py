import threading
import logging

from twitter.twitter_util import send_direct_message, send_direct_message_with_media, get_sender_id, delete_direct_message, upload_media


class MessageWorker():

    def __init__(self, message):
        self.message = message

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        logging.info(f'run MessageWorker')

        sender_id = get_sender_id(self.message)

        try:

            # media = upload_media(media='/files/thankyou.png')
            # reply = send_direct_message_with_media(sender_id, "Hello from Beppe", attachment_media_id = media.media_id)

            reply = send_direct_message(sender_id, "Hello from Beppe")

        except Exception as e:
            logging.info(f'Error {e}')

        # delete own reply
        delete_direct_message(reply)


