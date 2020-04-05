import os
import home
import keygen


def initialize():
    """Function to initialize the needed parameters"""
    # Generate the home directory
    home.home_generate()
    homedir = home.get_home()

    # Grab an email id and passphrase
    print("Enter an email ID: ")
    email = input()
    print("Enter a passphrase: ")
    passphrase = input()

    # Generate the key with the data
    key = keygen.generate_key(homedir, email, passphrase)
    print(key)


initialize()
