from algorithms.unix import (
    join_with_slash,
    full_path
)
import os
import unittest
class TestUnixPath(unittest.TestCase):
    def test_join_with_slash(self):
        self.assertEqual("path/to/dir/file", join_with_slash("path/to/dir/", "file"))
        self.assertEqual("path/to/dir/file", join_with_slash("path/to/dir", "file"))
        self.assertEqual("http://algorithms/part", join_with_slash("http://algorithms", "part"))
        self.assertEqual("http://algorithms/part", join_with_slash("http://algorithms/", "part"))

    def test_full_path(self):
        file_name = "file_name"
        # Test full path relative
        expect_path = "{}/{}".format(os.getcwd(), file_name)
        self.assertEqual(expect_path, full_path(file_name))
        # Test full path with expanding user
        # ~/file_name
        expect_path = "{}/{}".format(os.path.expanduser('~'), file_name)
        self.assertEqual(expect_path, full_path("~/{}".format(file_name)))
