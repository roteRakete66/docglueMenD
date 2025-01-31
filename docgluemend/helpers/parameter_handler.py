# parameter_handler.py
import os
import sys


def get_parameters():
    parameter_count = len(sys.argv) - 1
    for i, arg in enumerate(sys.argv):
        print(f"Parameter {i}: {arg}")

    return parameter_count


def permission(file_path):
    if not os.path.exists(file_path):
        return True
    while True:
        response = input(
            f'The file "{file_path}" already exists. Do you want to overwrite it? (y/n): '
        )
        if response.lower() == "y":
            return True
        if response.lower() == "n":
            print("Abort")
            return False
        print('Invalid input. Please enter "y" (yes) or "n" (no).')
