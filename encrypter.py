import gnupg
import home


def encrypt(plaintext, email):
    """This class will encrypt the plaintext"""

    gpg = gnupg.GPG(gnupghome=home.get_home())
    ciphertext_object = gpg.encrypt(plaintext, email)
    ciphertext_string = str(ciphertext_object)
    return ciphertext_string
