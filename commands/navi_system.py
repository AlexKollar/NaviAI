#!/bin/python3
import subprocess
from navi_shell import get_ai_name, tr
from navi import get_command_path

command = "navi_sys"
use = "Execute system command created by Navi"


def run(arguments=None):
    navi_command = arguments.replace("TERMINAL OUTPUT", "", 1).strip()
    base_command = navi_command.split()[0]
    if get_command_path(base_command) is not None:
        tr(f"\nDo I have your permission to use your **shell** to execute the following: \n\n{navi_command}\n")
        user_input = input(f"Do you want me to continue (y/n): ").strip().lower()
        if user_input == 'y':
            result = subprocess.run(
                navi_command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            output = f"Output: \n{result.stdout}" if result.stdout else ""
            tr(f"\nDone! {output}")
        else:
            tr(f"\nUnderstood! I will not execute the command.")
    else:
        tr(f"\nSorry, it looks like {base_command} is not installed on your system.")
