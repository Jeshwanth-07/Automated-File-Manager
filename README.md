This project is a Python script that automates file organization by monitoring a designated folder (like your Downloads folder) and sorting incoming files into categorized subfolders such as Audio, Video, Images, Documents, Applications, and Archives.

What It Does
--> Continuously watches a folder for new or modified files using the Watchdog library.
--> Automatically detects file types based on their extensions.
--> Moves files into appropriate subfolders, creating them if they don’t already exist.
--> Handles duplicate filenames gracefully by renaming files to avoid overwriting.
--> Keeps your folder clean and organized without manual effort.

Technologies Used:
--> Python 3.x
--> Watchdog (for filesystem event monitoring)
--> OS and Shutil modules (for file operations)
--> Logging module (for operation tracking)

How to Use:
--> Install required packages:
        pip install watchdog
--> Update the script’s source_dir and destination folder paths to match your setup.
--> Run the script:
      python automated_file_manager.py
--> The script will start watching the specified folder and automatically organize files as they arrive.

Why Use This?
--> If your Downloads or any other folder gets cluttered often, this tool saves you time by managing file sorting for you automatically. It’s lightweight, customizable, and easy to run in the background.

Notes:
-->Currently supports common file extensions for audio, video, images, documents, applications, and archives.
-->You can easily add more file types by updating the extension lists in the script.
-->The script runs indefinitely until manually stopped (Ctrl+C).

Possible Improvements:
--> Add support for more file types and extensions.
--> Implement a GUI for easier configuration.
--> Add logging to a file instead of console only.
--> Schedule the script to run as a background service on system startup.
