# Import necessary modules and functions
import os
import pip
import subprocess
import sys

# Function to handle installation process
def install_dependencies():
    # List of required dependencies
    dependencies = ["dependency1", "dependency2"]
    
    # Install each dependency individually
    for dependency in dependencies:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])
            print(f"Successfully installed {dependency}")
        except Exception as e:
            print(f"Failed to install {dependency}: {e}. Please check if the dependency is correctly spelled and available.")

# Call the install_dependencies function
if __name__ == "__main__":
    while True:
        user_confirmation = input("Do you want to install dependencies? (yes/no): ")
        if user_confirmation.lower() == 'yes':
            install_dependencies()
            break
        elif user_confirmation.lower() == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")