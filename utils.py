import zipfile

def toAscii(str):
    """Helper function to remove unicode characters from string.

    Args:
        str (str): String to filter

    Returns:
        str: Filtered string
    """
    return str.encode("ascii", "ignore").decode()

def unzip(src, dest):
    """Helper function to unzip files.

    Args:
        src (Path): Location of zip file to unzip
        dest (Path): Destination for zip file contents
    """
    with zipfile.ZipFile(src) as zf:
        zf.extractall(dest)