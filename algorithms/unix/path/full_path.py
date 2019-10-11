"""
Get a full absolute path a file
"""
import os
def full_path(file):
    return os.path.abspath(os.path.expanduser(file))
