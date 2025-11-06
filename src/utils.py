import os

def shorten_path(path:str) -> str:
    if not path:
        return ""
    return os.path.basename(path)