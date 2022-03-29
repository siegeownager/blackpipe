import gnupg
import logging
import sys

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_key(gpghome):
    """Function to generate the key pair"""
    gpg = gnupg.GPG(gnupghome=gpghome)
    print("Enter an email ID: ")
    email = input()
    print("Enter a passphrase: ")
    passphrase = input()
    input_data = generate_key_input(gpg, email, passphrase)
    gpg.gen_key(input_data)


def generate_key_input(gpg, email, passphrase):
    """Function to generate the input data object"""
    input_data = gpg.gen_key_input(name_email=email, passphrase=passphrase)
    return input_data


def export_key(gpg, key, passphrase):
    """Function to export the key pair"""

    strkey = str(key)
    public_key = gpg.export_keys(strkey, False)
    private_key = gpg.export_keys(strkey, True, passphrase=passphrase)

    with open('public.key', 'w') as f:
        f.write(public_key)

    with open('private.key', 'w') as f:
        f.write(private_key)

    logging.debug("Successfully exported keys!")


def list_public_keys(gpghome):
    """This function will list the current public gpg keys in the gpg home directory"""

    gpg = gnupg.GPG(gnupghome=gpghome)
    public_keys = gpg.list_keys()
    print(public_keys)


def list_private_keys(gpghome):
    """This function will list the current private gpg keys in the gpg home directory"""

    gpg = gnupg.GPG(gnupghome=gpghome)
    private_keys = gpg.list_keys(True)  # Passing True as parameter makes it return private keys
    print(private_keys)
