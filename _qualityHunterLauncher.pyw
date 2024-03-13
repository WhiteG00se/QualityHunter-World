import os
import tkinter as tk
import subprocess
import requests
import re

# Define minimum width and height for the popup window
MIN_WIDTH = 350
MIN_HEIGHT = 150

def fetch_local_version():
    # Check if "version.txt" exists in the current directory
    if os.path.isfile("version.txt"):
        # Read the content of the file
        with open("version.txt", "r") as f:
            version_string = f.read().strip()
            # Validate version format
            if re.match(r'^\d+(\.\d+)+$', version_string):
                # Extract version number
                return version_string
            else:
                return "error"
    else:
        return "error"

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
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Check if "MonsterHunterWorld.exe" exists in the current directory
    if os.path.isfile("MonsterHunterWorld.exe"):
        # Execute the game without showing cmd window
        subprocess.Popen(["start", "MonsterHunterWorld.exe"], shell=True)
    else:
        print("Error: 'MonsterHunterWorld.exe' not found in the current directory.")

def create_popup():
    # Set the working directory to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Fetch local and latest versions
    local_version = fetch_local_version()
    latest_version = fetch_latest_version()

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
        root.destroy()  # Close the window
        run_game()  # Run the game

    # Function to exit the program
    def exit_program():
        root.destroy()

    # Function to update the game
    def update_game():
        pass  # Placeholder for future functionality

    # Compare versions and decide action
    if local_version == latest_version:
        button_text = "Start Game (Enter)"
        command = start_game
        root.bind("<Return>", lambda event: start_game())
    elif local_version < latest_version:
        button_text = "Update (Enter)"
        command = update_game
        root.bind("<Return>", lambda event: update_game())
    else:
        button_text = "Version Error, Exit (Enter)"
        command = exit_program
        root.bind("<Return>", lambda event: exit_program())

    # Display button (if applicable)
    if command:
        start_button = tk.Button(root, text=button_text, command=command)
        start_button.pack(padx=20, pady=5)

    # Add exit button
    exit_button = tk.Button(root, text="Exit (Esc)", command=exit_program)
    exit_button.pack(padx=20, pady=5)

    root.bind("<Escape>", lambda event: exit_program())

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_popup()
