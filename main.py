import os
import home
import keygen
import encrypter

FIRSTRUN = True


def initialize():
    """Function to initialize the needed parameters"""
    # Generate the home directory
    home.home_generate()

    # Grab an email id and passphrase
    print("Enter an email ID: ")
    email = input()
    print("Enter a passphrase: ")
    passphrase = input()

    # Generate the key with the data
    keygen.generate_key(home.get_home(), email, passphrase)


def encrypt():
    email = 'test@test.com'
    plaintext = 'Test string to encrypt'
    ciphertext = encrypter.encrypt(plaintext, email)
    print(ciphertext)


if FIRSTRUN:
    initialize()

encrypt()