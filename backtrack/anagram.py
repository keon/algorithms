import unittest

def all_perms_iter(elements):
    """
        iterator: returns a perumation by each call. 
    """
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms_iter(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def all_perms(elements):
    """
        returns a list with the permuations.
    """
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp


def anagram(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for c in s1:
        pos = ord(c)-ord('a')
        c1[pos] = c1[pos] + 1

    for c in s2:
        pos = ord(c)-ord('a')
        c2[pos] = c2[pos] + 1

    return c1 == c2


class TestSuite (unittest.TestCase):

    def test_all_perms(self):
        perms = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
        self.assertEqual(perms, all_perms("abc"))

    def test_all_perms_iter(self):
        it = all_perms_iter("abc")
        perms = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
        for i in range(len(perms)):
            self.assertEqual(perms[i], next(it))

    def test_angram(self):
        self.assertTrue(anagram('apple', 'pleap'))
        self.assertFalse(anagram("apple", "cherry"))


if __name__ == "__main__":
    unittest.main()
