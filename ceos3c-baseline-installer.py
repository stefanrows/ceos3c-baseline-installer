# --------------
# Imports
# --------------
import os
import getpass
# --------------
# Get Username
user = getpass.getuser()
# -
# Colors
colorGreen = "\033[1; 32; 40m end="""
# -
# --------------
# Functions
# --------------

# Update & Upgrade


def upgrade():
    os.system('sudo apt update && sudo apt upgrade')
# -

# Add new User


def addUser():
    print("### Creating a Low Priv User ###")
    user = input("Choose a username: ")
    os.system('sudo adduser ' + user)
    print("### Adding new user to Sudo ###")
    os.system("sudo usermod -aG sudo " + user)
    os.system("sudo chsh -s /bin/bash " + user)
    print("### Done ###")
    print("### Switching to new user... ###")
    os.system("su " + user)
    print("### Done! Welcome {}".format(user))


# --------------
# Function Calls
# --------------
upgrade()
addUser()
# -
