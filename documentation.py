# Documentation for Sweep

def installation_section():
    """
    Provides instructions for installing Sweep using pip.
    """
    return "\n".join([
        "To install Sweep, use the following command:",
        "pip install sweep",
        ""
    ])

def usage_section():
    """
    Provides instructions on how to use Sweep in GitHub repositories.
    """
    return "\n".join([
        "To use Sweep in your GitHub repositories, follow these steps:",
        "1. Clone the repository where you want to use Sweep.",
        "2. Install Sweep using the command 'pip install sweep'.",
        "3. Configure Sweep by updating the sweep.yaml file with your desired settings.",
        "4. Run Sweep using the command 'python app.py'.",
        "5. Sweep will now analyze your code and generate bug fixes or feature requests as needed.",
        ""
    ])

def main():
    # Call the sections to display the instructions
    return installation_section() + "\n" + usage_section()

if __name__ == "__main__":
    print(main())