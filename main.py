import os
import sys

import home
import keygen
import encrypter
import decrypter
import base64_handler


def initialize():
    """Function to initialize the needed parameters"""
    # Generate the home directory
    home.home_generate()


def main():
    initialize()
    print("Hello!")

    while True:
        print("What would you like to do?")
        print("1 - Generate a new personal key pair")
        print("2 - View existing public keys")
        print("3 - View existing private keys")
        print("9 - Exit")

        print("Enter number to select option (1-9): ", end=' ')

        selection = input()

        if selection == '1':
            keygen.generate_key(home.get_home())
        elif selection == '2':
            keygen.list_public_keys(home.get_home())
        elif selection == '3':
            keygen.list_private_keys(home.get_home())
        else:
            sys.exit()


if __name__ == "__main__":
    main()
