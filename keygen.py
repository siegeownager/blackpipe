import gnupg
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_key(gpghome, email, passphrase):
    """Function to generate the key pair"""
    gpg = gnupg.GPG(gnupghome=gpghome)
    input_data = generate_key_input(gpg, email, passphrase)
    key = gpg.gen_key(input_data)
    export_key(gpg, str(key), passphrase)
    return key


def generate_key_input(gpg, email, passphrase):
    """Function to generate the input data object"""
    input_data = gpg.gen_key_input(name_email=email, passphrase=passphrase)
    return input_data


def export_key(gpg, key, passphrase):
    """Function to export the key pair"""
    public_key = gpg.export_keys(key, False)
    private_key = gpg.export_keys(key, True, passphrase=passphrase)

    with open('public.key', 'w') as f:
        f.write(public_key)

    with open('private.key', 'w') as f:
        f.write(private_key)
