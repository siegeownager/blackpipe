import os
import home
import keygen
import encrypter
import decrypter
import base64_handler

FIRSTRUN = False # Boolean variable for testing purposes

home.home_generate()

def initialize():
    """Function to initialize the needed parameters"""
    # Generate the home directory

    # Grab an email id and passphrase
    print("Enter an email ID: ")
    email = input()
    print("Enter a passphrase: ")
    passphrase = input()

    # Generate the key with the data
    keygen.generate_key(home.get_home(), email, passphrase)


# This only exists for testing purposes
if FIRSTRUN:
    initialize()


def do_stuff():
    """Function to test out our changes"""



do_stuff()