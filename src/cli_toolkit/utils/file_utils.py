from pathlib import Path


def file_exists(filepath):
    path = Path(filepath)
    return path.exists()


def read_file(filepath):
    path = Path(filepath)
    return path.read_text()


def create_folder(folderpath):
    path = Path(folderpath)
    path.mkdir(parents=True, exist_ok=True)
