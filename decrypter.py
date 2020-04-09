import gnupg
import home


def decrypt(ciphertext, passphrase):
    """This class will decrypt the ciphertext"""

    gpg = gnupg.GPG(gnupghome=home.get_home())
    plaintext = gpg.decrypt(ciphertext, passphrase=passphrase)
    plaintext_string = str(plaintext)
    return plaintext_string
