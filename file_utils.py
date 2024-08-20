import os
import shutil

def copy_file(src, dest):
    """
    Copies a file from the source path to the destination path.

    Args:
        src (str): The path to the source file.
        dest (str): The path to the destination file.

    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are permission issues preventing the copy.
        IOError: For other file-related errors during the copy process.
    """
    try:
        shutil.copy2(src, dest)  # copy2 preserves metadata (timestamps, etc.)
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file not found: {src}")
    except PermissionError:
        raise PermissionError(f"Permission denied to copy file: {src}")
    except IOError as e:
        raise IOError(f"Error copying file: {e}")

def move_file(src, dest):
    """
    Moves a file from the source path to the destination path.

    Args:
        src (str): The path to the source file.
        dest (str): The path to the destination file.

    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are permission issues preventing the move.
        IOError: For other file-related errors during the move process.
    """
    try:
        shutil.move(src, dest)
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file not found: {src}")
    except PermissionError:
        raise PermissionError(f"Permission denied to move file: {src}")
    except IOError as e:
        raise IOError(f"Error moving file: {e}")

def delete_file(path):
    """
    Deletes a file at the specified path.

    Args:
        path (str): The path to the file to be deleted.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there are permission issues preventing the deletion.
        OSError: For other operating system-related errors during the deletion.
    """
    try:
        os.remove(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except PermissionError:
        raise PermissionError(f"Permission denied to delete file: {path}")
    except OSError as e:
        raise OSError(f"Error deleting file: {e}")

def walk_directory(path):
    """
    Recursively walks through a directory and its subdirectories, yielding tuples of
    (root, dirs, files) for each directory encountered.

    Args:
        path (str): The path to the directory to walk.

    Yields:
        tuple: A tuple containing:
            - root (str): The current directory path.
            - dirs (list): A list of subdirectory names in the current directory.
            - files (list): A list of file names in the current directory.
    """
    for root, dirs, files in os.walk(path):
        yield root, dirs, files

def get_file_size(path):
    """
    Returns the size of a file in bytes.

    Args:
        path (str): The path to the file.

    Returns:
        int: The size of the file in bytes.

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: For other operating system-related errors.
    """
    try:
        return os.path.getsize(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except OSError as e:
        raise OSError(f"Error getting file size: {e}")

def get_file_extension(path):
    """
    Returns the file extension (including the dot) from a file path.

    Args:
        path (str): The path to the file.

    Returns:
        str: The file extension (e.g., ".txt", ".pdf") or an empty string if no extension is found.
    """
    return os.path.splitext(path)[1]
