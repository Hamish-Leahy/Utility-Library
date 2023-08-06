import os
import shutil

def cleanup_desktop(desktop_path, target_folders):
    """
    Automates the cleanup process of the desktop by moving files to designated folders.

    Parameters:
    desktop_path (str): The path to the user's desktop.
    target_folders (dict): A dictionary containing folder names as keys and their corresponding file extensions as values.
                           Files with matching extensions will be moved to the corresponding folder.

    Returns:
    None
    """
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)

        # Skip directories and hidden files
        if os.path.isdir(item_path) or item.startswith('.'):
            continue

        # Get the file extension (if any)
        _, file_ext = os.path.splitext(item)

        # Find the target folder for the file extension
        target_folder = None
        for folder, extensions in target_folders.items():
            if file_ext in extensions:
                target_folder = folder
                break

        # If the target folder exists, move the file to it
        if target_folder:
            target_path = os.path.join(desktop_path, target_folder)
            os.makedirs(target_path, exist_ok=True)
            shutil.move(item_path, os.path.join(target_path, item))

if __name__ == "__main__":
    desktop_path = os.path.expanduser("~/Desktop")

    # Customize your target folders and file extensions here
    target_folders = {
        "Documents": [".txt", ".doc", ".docx", ".pdf", ".xlsx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Other": []  # Add other file extensions that don't fit in the above categories
    }

    cleanup_desktop(desktop_path, target_folders)
