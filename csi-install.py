#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports.
import sys  # System stuff.
import os  # Operating System functions.

user = os.environ['HOME']
path = f'{user}/.bashrc'

print("Cleaning up....")


def main():
    # Check for updates
    # from src import Update
    # Update()

    # List over commands to run
    commands = []

    # Navi related commands
    commands += [
        # add navi alias to bashrc
        f'echo "alias navi=\'python3 /opt/Navi/navi.py\'" >> {path}',
        'sudo apt install -y python3 python3-pip python-dev nmap macchanger clamav clamav-daemon',
        'sudo systemctl stop clamav-freshclam',
        'sudo freshclam',
        'sudo systemctl start clamav-freshclam',
        'sudo rm -rf /opt/Navi',
        'sudo mkdir /opt/Navi',
        'sudo cp -r . /opt/Navi',
        'sudo cp desktop/navi.desktop /usr/share/applications/navi.desktop',
        'sudo rm -rf /opt/Navi/.git/',
        'sudo rm -rf /opt/Navi/.github/',
        'sudo rm /opt/Navi/README.md',
        'sudo rm /opt/Navi/CONTRIBUTING.md',
        'sudo rm /opt/Navi/CODE_OF_CONDUCT.md',
        'sudo rm /opt/Navi/install.py',
        'sudo chmod -R 777 /opt/Navi',
    ]

    # Run the commands
    for c in commands:
        if len(c) <= 0:
            continue
        os.system(c)

    exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nYou interrupted the program.')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)