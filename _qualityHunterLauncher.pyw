import os
import sys
import tkinter as tk
import subprocess
import requests
import re
import cffi
import _cffi_backend

# Define minimum width and height for the popup window
MIN_WIDTH = 350
MIN_HEIGHT = 150

def get_application_path():
    # Check if running as a PyInstaller bundle (compiled exe)
    if getattr(sys, 'frozen', False):
        # If so, use the directory where the executable is located
        application_path = os.path.dirname(sys.executable)
    else:
        # If not, use the directory of the script
        application_path = os.path.dirname(os.path.abspath(__file__))
    return application_path


def fetch_local_version():
    # Check if "version.txt" exists in the current directory
    version_file = os.path.join(get_application_path(), "version.txt")
    if os.path.isfile(version_file):
        # Read the content of the file
        with open(version_file, "r") as f:
            version_string = f.read().strip()
            # Validate version format
            if re.match(r'^\d+(\.\d+)+$', version_string):
                # Extract version number
                return version_string
            else:
                return "error"
    else:
        return "missing"

def fetch_latest_version():
    # Fetch the latest version from the GitHub repository
    url = "https://raw.githubusercontent.com/WhiteG00se/QualityHunter/main/version.txt"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            version_string = response.text.strip()
            # Validate version format
            if re.match(r'^\d+(\.\d+)+$', version_string):
                # Extract version number
                return version_string
            else:
                return "error"
        else:
            return "error"
    except Exception as e:
        print(f"Error fetching latest version: {e}")
        return "error"

def run_game():
    # Set the working directory to the script's directory
    os.chdir(get_application_path())

    # Check if "MonsterHunterWorld.exe" exists in the current directory
    if os.path.isfile("MonsterHunterWorld.exe"):
        # Execute the game without showing cmd window
        subprocess.Popen(["start", "MonsterHunterWorld.exe"], shell=True)
    else:
        print("Error: 'MonsterHunterWorld.exe' not found in the current directory.")

def create_popup():
    # Set the working directory to the script's directory
    os.chdir(get_application_path())

    # Fetch local and latest versions
    local_version = fetch_local_version()
    latest_version = fetch_latest_version()
    print(get_application_path())
    # Create the root window
    root = tk.Tk()
    root.title("Quality Hunter: Version Checker")
    root.minsize(MIN_WIDTH, MIN_HEIGHT)

    # Display local and latest version numbers
    local_version_label = tk.Label(root, text=f"Local Version: {local_version}")
    local_version_label.pack(padx=20, pady=5)

    latest_version_label = tk.Label(root, text=f"Latest Version: {latest_version}")
    latest_version_label.pack(padx=20, pady=5)

    # Function to start the game
    def start_game():
        exit_launcher()
        run_game()  # Run the game

    # Function to exit the program
    def exit_launcher():
        root.destroy()

    # Function to update the game
    def download_latest_zip():
    # URL of the repository's latest zip file
        zip_url = "https://github.com/WhiteG00se/QualityHunter/archive/refs/heads/main.zip"

        # Path where you want to save the downloaded zip
        download_path = os.path.join(get_application_path(), "latest_version.zip")

        # Make the request and save the zip file
        try:
            response = requests.get(zip_url)
            response.raise_for_status()  # Check if the request was successful

            # Write the content of the response to a zip file
            with open(download_path, "wb") as zip_file:
                zip_file.write(response.content)

            print(f"Download successful. File saved to {download_path}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while downloading the zip file: {e}")
        exit_launcher()

    # Compare versions and decide action
    if local_version == latest_version:
        button_text = "Start Game (Enter)"
        command = start_game
        root.bind("<Return>", lambda event: start_game())
    elif local_version < latest_version or local_version=='missing':
        button_text = "Download Latest .zip (Enter)"
        command = download_latest_zip
        root.bind("<Return>", lambda event: download_latest_zip())
    else:
        button_text = "Version Error, Exit (Enter)"
        command = exit_launcher
        root.bind("<Return>", lambda event: exit_launcher())

    # Display button (if applicable)
    if command:
        start_button = tk.Button(root, text=button_text, command=command)
        start_button.pack(padx=20, pady=5)

    # Add exit button
    exit_button = tk.Button(root, text="Exit (Esc)", command=exit_launcher)
    exit_button.pack(padx=20, pady=5)

    root.bind("<Escape>", lambda event: exit_launcher())

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_popup()
