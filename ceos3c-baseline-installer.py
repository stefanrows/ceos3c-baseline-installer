# --------------
# Imports
# --------------
import os
import getpass
# --------------
# Get Username
# user = getpass.getuser()
# Add new User
print("### Creating a Low Priv User ###")
user = input("Choose a Username for your Low-Priv User: ")
# -
# Colors
colorGreen = "\033[1; 32; 40m end="""
# -
# --------------
# Functions
# --------------

# Update & Upgrade


def upgrade():
    os.system('sudo apt update && sudo apt upgrade -y')
# -


def addUser():

    os.system('sudo adduser ' + user)
    print("### Adding new user to Sudo ###")
    os.system("sudo usermod -aG sudo " + user)
    os.system("sudo chsh -s /bin/bash " + user)
    print("### Done! Welcome {}".format(user))
# -


def installTools():
    # Default Tools
    print("### Installing Default Tools ###")
    os.system(
        'sudo -u {} sudo apt install nixnote2 nautilus-dropbox keepassxc python3-pip -y'.format(user))
    # VSCode
    print("### Installing Visual Studio Code ###")
    os.system(
        'sudo -u {} sudo apt install software-properties-common apt-transport-https wget -y'.format(user))
    os.system('sudo -u {} wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -'.format(user))
    os.system(
        'sudo -u {} sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"'.format(user))
    os.system('sudo -u {} sudo apt update && sudo apt install code -y'.format(user))

# Cleaning Up


def cleanup():
    print("### Cleaning up APT ###")
    os.system(
        'sudo -u {} sudo apt autoremove -y && sudo apt autoclean -y'.format(user))


# --------------
# Function Calls
# --------------


addUser()
upgrade()
installTools()
cleanup()
# -
