import os

home_directory = ''


def home_generate():
    global home_directory
    current_directory = os.getcwd()
    home_directory = os.path.join(current_directory, "gpghome")


def get_home():
    global home_directory
    return home_directory


