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
# Changing Keyboard Layout
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
        'sudo -u {} sudo apt install apt-transport-https -y'.format(user))
    os.system('sudo -u {} curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg'.format(user))
    os.system(
        'sudo -u {} sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/'.format(user))
    os.system(
        'sudo -u {} sudo sh -c \'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list\''.format(user))
    os.system('sudo -u {} sudo apt update && sudo apt install code -y'.format(user))

# -

# --------------
# Installing Optional Tools
# --------------


def installOptTools():
    nordVPN = input("[x] Do you want to install NordVPN [x] (y/N): ")
    if nordVPN.lower() == "y":
        print("We are installing it!")
        print(Fore.GREEN + "### Installing NordVPN ###")
        print(Style.RESET_ALL)
        os.system(
            'sudo -u {} sudo wget -qnc https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb'.format(user))
        os.system(
            'sudo -u {} sudo dpkg -i /pathToFile/nordvpn-release_1.0.0_all.deb'.format(user))
        os.system(
            'sudo -u {} sudo apt update'.format(user))
        os.system(
            'sudo -u {} sudo apt install nordvpn'.format(user))
    else:
        print("Not going to install NordVPN...Skipping...")
# -


# --------------
# Change Root Pwd
# --------------
# To Do
# -

# --------------
# Cleaning Up
# --------------


def cleanup():
    print(Fore.GREEN + "### Cleaning up APT ###")
    print(Style.RESET_ALL)
    os.system(
        'sudo -u {} sudo apt autoremove -y && sudo apt autoclean -y'.format(user))
# -

# --------------
# Function Calls
# --------------


# addUser()
# changeKeyboardLayout()
# upgrade()
# installTools()
installOptTools()
# cleanup()
# -
