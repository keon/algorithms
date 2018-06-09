from algorithms.unix import (
    join_with_slash
)
import unittest
class TestUnixPath(unittest.TestCase):
    def test_join_with_slash(self):
        self.assertEqual("path/to/dir/file", join_with_slash("path/to/dir/", "file"))
        self.assertEqual("path/to/dir/file", join_with_slash("path/to/dir", "file"))
        self.assertEqual("http://algorithms/part", join_with_slash("http://algorithms", "part"))
        self.assertEqual("http://algorithms/part", join_with_slash("http://algorithms/", "part"))
