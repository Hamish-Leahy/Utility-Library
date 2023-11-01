# desktop quick cleaner

import os
import shutil

# Define the path for the desktop
DESKTOP_PATH = os.path.expanduser("~/Desktop")

# Define categories and their respective file extensions
CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.md', '.odt', '.ods'],
    'Audio': ['.mp3', '.wav', '.m4a', '.flac', '.ogg'],
    'Video': ['.mp4', '.mkv', '.flv', '.mpeg', '.avi', '.mov'],
    'Compressed': ['.zip', '.rar', '.tar', '.gz', '.bz2'],
    'Executables': ['.exe', '.sh', '.bat', '.jar'],
    'Others': []
}

def organize_files():
    for filename in os.listdir(DESKTOP_PATH):
        file_path = os.path.join(DESKTOP_PATH, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            moved = False
            for category, extensions in CATEGORIES.items():
                if file_extension in extensions:
                    category_path = os.path.join(DESKTOP_PATH, category)
                    if not os.path.exists(category_path):
                        os.mkdir(category_path)
                    shutil.move(file_path, category_path)
                    moved = True
                    break
            if not moved:  # If file didn't fit into any category
                category_path = os.path.join(DESKTOP_PATH, "Others")
                if not os.path.exists(category_path):
                    os.mkdir(category_path)
                shutil.move(file_path, category_path)

if __name__ == "__main__":
    organize_files()
