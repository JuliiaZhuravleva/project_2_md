import os

def get_relative_path(base_path: str, full_path: str) -> str:
    return os.path.relpath(full_path, base_path)

def is_binary_file(filepath: str) -> bool:
    """
    Returns True if the file is binary, False otherwise.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            file.read()
        return False
    except UnicodeDecodeError:
        return True