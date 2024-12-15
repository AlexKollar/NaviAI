import os

import navi_internal
from navi_shell import restart_navi

command = "settings"
use = "Review and modify the Navi settings"
aliases = ['--settings']

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.abspath(os.path.join(script_dir, "..", "..", "config"))
default_config_path = os.path.abspath(os.path.join(script_dir, "..", "..", "default_config"))


def create_config(default_values):
    if not os.path.exists(config_path):
        with open(config_path, "w") as file:
            for key, value in default_values.items():
                file.write(f"{key}={value}\n")


def modify_config(key, value):
    if not os.path.exists(config_path):
        print(f"Unable to modify file at {config_path}.")
        return

    with open(config_path, "r") as file:
        lines = file.readlines()

    modified = False
    with open(config_path, "w") as file:
        for line in lines:
            if line.startswith("#") or "=" not in line.strip():
                file.write(line)
                continue

            current_key, current_value = line.strip().split("=", 1)
            if current_key == key:
                file.write(f"{key}={value}\n")
                modified = True
            else:
                file.write(line)

        # Add the key-value pair if it doesn't exist
        if not modified:
            file.write(f"{key}={value}\n")


def read_config(config_path):
    if not os.path.exists(config_path):
        print(f"Config file not found at {config_path}.")
        return {}

    config = {}
    with open(config_path, "r") as file:
        for line in file:
            if line.startswith("#") or not line.strip():
                continue

            if "=" in line:
                key, value = line.strip().split("=", 1)
                value = value.split("#", 1)[0].strip()
                if value.lower() == "true":
                    value = True
                elif value.lower() == "false":
                    value = False
                config[key.strip()] = value
    return config


def settings_init():
    if os.path.exists(config_path):
        return read_config(config_path)
    else:
        import getpass
        default_config = read_config(default_config_path)
        create_config(default_config)
        modify_config("username", getpass.getuser())
        return read_config(config_path)


def run(arguments=None):
    navi_instance = navi_internal.navi_instance

    current_settings = settings_init()

    while True:
        navi_instance.clear_terminal()
        print("\nCurrent Settings:")
        for key, value in current_settings.items():
            print(f"  {key}: {value}")

        print("\nOptions:")
        print("  [1] Update a setting")
        print("  [2] Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            key_to_modify = input("Enter the setting key to update: ").strip()
            if key_to_modify in current_settings:
                new_value = input(
                    f"Enter the new value for '{key_to_modify}' (current: {current_settings[key_to_modify]}): ").strip()
                modify_config(key_to_modify, new_value)
                print(f"'{key_to_modify}' updated successfully!")
                current_settings = settings_init()
            else:
                print(f"Error: '{key_to_modify}' is not a valid setting.")
        elif choice == "2":
            restart_navi()
            break
        else:
            print("Invalid choice. Please try again.")