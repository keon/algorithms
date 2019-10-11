"""
Splitting a path into 2 parts
Example:
Input: https://algorithms/unix/test.py   (for url)
Output:
    part[0]: https://algorithms/unix
    part[1]: test.py

Input: algorithms/unix/test.py          (for file path)
Output:
    part[0]: algorithms/unix
    part[1]: test.py
"""
import os

def split(path):
    parts = []
    split_part = path.rpartition('/')
    # Takt the origin path without the last part
    parts.append(split_part[0])
    # Take the last element of list
    parts.append(split_part[2])
    return parts
