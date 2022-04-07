import gnupg
import home
import logging
import base64_handler

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def encrypt(plaintext, email):
    """This function will encrypt the plaintext"""

    gpg = gnupg.GPG(gnupghome=home.get_home())
    ciphertext_object = gpg.encrypt(plaintext, email)
    ciphertext_string = str(ciphertext_object)
    return ciphertext_string


def message_sign(message, id):
    """This function is used for signing our message with the private key"""

    gpg = gnupg.GPG(gnupghome=home.get_home())
    signed_data = gpg.sign(message, keyid=id)
    if len(str(signed_data)) == 0:
        print("ERROR: Verify that the key exists")
    else:
        print(base64_handler.data_to_base64(str(signed_data)))
