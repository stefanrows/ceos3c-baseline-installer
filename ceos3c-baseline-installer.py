# --------------
# Imports
# --------------
import os
from colorama import Fore, Back, Style
# -
# --------------
# Functions
# --------------

# Add new Low Privilege User Account

print(Fore.GREEN + "### Creating a Low Priv User ###")
print(Style.RESET_ALL)
user = input("Choose a Username for your Low-Priv User: ")


def addUser():

    os.system('sudo adduser ' + user)
    print(Fore.GREEN + "### Adding new user to Sudo ###")
    print(Style.RESET_ALL)
    os.system("sudo usermod -aG sudo " + user)
    os.system("sudo chsh -s /bin/bash " + user)
    print(Fore.GREEN + "### Done! Welcome {}".format(user))
    print(Style.RESET_ALL)
# -

# --------------
# Changing Keyboard Layout to German
# --------------


def changeKeyboardLayout():
    print(Fore.GREEN + "### Changing Keyboard Layout ###")
    print(Style.RESET_ALL)
    os.system(
        'sudo -u {} sudo dpkg-reconfigure keyboard-configuration'.format(user))
    os.system(
        'sudo -u {} sudo service keyboard-setup restart'.format(user))
# -

# --------------
# Update & Upgrade
# --------------


def upgrade():
    print(Fore.GREEN + "### Updating & Upgrading the System ###")
    print(Style.RESET_ALL)
    os.system('sudo apt update && sudo apt upgrade -y')
# -

# --------------
# Installing Tools
# --------------


def installTools():
    # Default Tools
    print(Fore.GREEN + "### Installing Default Tools ###")
    print(Style.RESET_ALL)
    os.system(
        'sudo -u {} sudo apt install nixnote2 nautilus-dropbox keepassxc python3-pip -y'.format(user))
    # VSCode
    print(Fore.GREEN + "### Installing Visual Studio Code ###")
    print(Style.RESET_ALL)
    os.system(
        'sudo -u {} sudo apt install software-properties-common apt-transport-https wget -y'.format(user))
    os.system('sudo -u {} wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -'.format(user))
    os.system(
        'sudo -u {} sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"'.format(user))
    os.system('sudo -u {} sudo apt update && sudo apt install code -y'.format(user))
# -
# --------------
# Cleaning Up
# --------------

# -


def cleanup():
    print(Fore.GREEN + "### Cleaning up APT ###")
    print(Style.RESET_ALL)
    os.system(
        'sudo -u {} sudo apt autoremove -y && sudo apt autoclean -y'.format(user))


# --------------
# Function Calls
# --------------


addUser()
changeKeyboardLayout()
upgrade()
installTools()
cleanup()
# -
