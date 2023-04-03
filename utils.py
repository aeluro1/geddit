import zipfile

def toAscii(str):
    """Helper function to remove unicode characters from string

    Args:
        str (str): String to filter

    Returns:
        str: Filtered string
    """
    return str.encode("ascii", "ignore").decode()

def unzip(src, dest):
    with zipfile.Zipfile(src) as zf:
        zf.extractall(dest)
