# Import necessary modules and functions
import os
import pip
import subprocess
import sys
import argparse

# Function to handle installation process
def install_dependencies(requirements_file):
    try:
        with open(requirements_file, 'r') as f:
            dependencies = f.read().splitlines()
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + dependencies)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies due to a non-zero exit code: {e}. Please check if the requirements file exists and is correctly formatted.")

# Call the install_dependencies function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Install dependencies.')
    parser.add_argument('--install-deps', action='store_true',
                        help='Install dependencies')
    args = parser.parse_args()

    if args.install_deps:
        install_dependencies("requirements.txt")