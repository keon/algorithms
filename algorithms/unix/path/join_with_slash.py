"""
Both URL and file path joins use slashes as dividers between their parts.
For example:

path/to/dir + file --> path/to/dir/file
path/to/dir/ + file --> path/to/dir/file
http://algorithms.com/ + part --> http://algorithms.com/part
http://algorithms.com + part --> http://algorithms/part
"""
import os

def join_with_slash(base, suffix):
    # Remove / trailing
    base = base.rstrip('/')
    # Remove / leading
    suffix = suffix.lstrip('/').rstrip()
    full_path = "{}/{}".format(base, suffix)
    return full_path
