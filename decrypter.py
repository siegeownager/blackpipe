import gnupg
import home
import logging
import base64_handler

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def decrypt(ciphertext, passphrase):
    """This class will decrypt the ciphertext"""

    gpg = gnupg.GPG(gnupghome=home.get_home())
    plaintext = gpg.decrypt(ciphertext, passphrase=passphrase)
    plaintext_string = str(plaintext)
    return plaintext_string


def message_verify(message):
    """This function will verify the message"""

    gpg = gnupg.GPG(gnupghome=home.get_home())
    base64_decoded_message = base64_handler.base64_to_data(message)

    verified = gpg.verify(base64_decoded_message)
    if not verified:
        print("Message could not be verified!")
    else:
        print("Message successfully verified!")
