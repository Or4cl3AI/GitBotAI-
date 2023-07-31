# Import necessary modules and functions
import os
import pip
import subprocess
import sys
import argparse

# Function to handle installation process
def install_dependencies(requirements_file):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
    except Exception as e:
        print(f"Failed to install dependencies from {requirements_file}: {e}")

# Call the install_dependencies function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Install dependencies.')
    parser.add_argument('--install-deps', action='store_true',
                        help='Install dependencies')
    args = parser.parse_args()

    if args.install_deps:
        install_dependencies("requirements.txt")