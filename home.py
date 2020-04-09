import os

home_directory = ''


def home_generate():
    """Function to generate the home directory path and create it if needed"""

    global home_directory
    current_directory = os.getcwd()
    home_directory = os.path.join(current_directory, "gpghome")
    if not os.path.exists(home_directory):
        os.mkdir(home_directory)


def get_home():
    """Function to grab the home directory path"""

    global home_directory
    return home_directory


