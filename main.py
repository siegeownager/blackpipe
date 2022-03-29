import os
import sys

import home
import keygen
import encrypter
import decrypter
import base64_handler


def gen_key_pair():
    """Function to initialize the needed parameters"""
    # Generate the home directory
    home.home_generate()

    # Generate the key with the data
    keygen.generate_key(home.get_home())


def main():
    print("Hello!")

    while True:
        print("What would you like to do?")
        print("1 - Generate a new personal key pair")
        print("2 - View existing keys")
        print("9 - Exit")

        print("Enter number to select option (1-9): ", end=' ')

        selection = input()

        if selection == '1':
            gen_key_pair()
        elif selection == '2':
            keygen.list_keys()
        else:
            sys.exit()


if __name__ == "__main__":
    main()
