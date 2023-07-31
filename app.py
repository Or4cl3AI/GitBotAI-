# Import necessary modules and functions
import os
import pip
import subprocess
import sys
import argparse

# Function to handle installation process
def install_dependencies():
    # Install required dependencies using pip
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except Exception as e:
        print(f"Failed to install dependencies: {e}. Please check if the dependencies are correctly spelled and available in requirements.txt.")

# Call the install_dependencies function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Install dependencies.')
    parser.add_argument('--install-deps', action='store_true',
                        help='Install dependencies')
    args = parser.parse_args()

    if args.install_deps:
        install_dependencies()