import unittest

def all_perms_iter(elements):
    """
        iterator: returns a perumation by each call. 
    """
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
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
        

def anagram(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    return c1 == c2


class TestSuite (unittest.TestCase):
    def test_all_perms(self):
        allPerms = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
        self.assertEqual(allPerms,all_perms("abc"))
    def test_all_perms_iter(self):
        it = all_perms_iter("abc")
        allPerms = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
        for i in range(len(allPerms)):
            self.assertEqual(allPerms[i],next(it))


if __name__ == "__main__":
    unittest.main()
