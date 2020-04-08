import os
import home
import keygen
import encrypter
import decrypter

FIRSTRUN = False
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


def encrypt():
    email = 'testing@test.com'
    plaintext = 'Test string to encrypt'
    ciphertext = encrypter.encrypt(plaintext, email)
    print(ciphertext)

def decrypt():
    passphrase = 'testing'
    ciphertext = """-----BEGIN PGP MESSAGE-----

hQEMA8y43EHkkTJvAQgArXlLHGdrlJLM/8JK4BCZX2Y4o9UxfF/52uh3bQrlmUZw
tYBfjkutpiklfnBDumnz9+M5jidKVX10FAhTWdut/KRJv5qLBjqzKby1vYlwH1gD
PCznTfs5zX3kxSMoa7nTdxAwlJP1lboTn0MNgBFf5DIAFD6M5XeRGSDlJ7bBdm7y
m7iFUYRCfbTw2DdxnOv2b4kfG7aU66azE0ODNC4yXk0PDmZbx6RzCEyGm7AcHmRd
K3E0Aj36vQ6WE/KwJd3gH8nJz76ugT8NG4dPDhcf0Aj6EYHqc7mjC3PYzX+5xwBi
zGF/V28oP5tsK5VenEY1wl/y8EInXi85ch4oqobEENJRAVujD2nE9GktIsN85P4J
ES0FoQGAOfO9YDOj5b5SSp5MDvXpc2jegAKXyPuy7LI4eRwU9+ybRg8wCS1ZzfcR
a1g9Slx+OFmOHAIECOFZbE5q
=qcc/
-----END PGP MESSAGE-----"""
    plaintext = decrypter.decrypt(ciphertext, passphrase)
    print(plaintext)



if FIRSTRUN:
    initialize()

encrypt()
decrypt()
