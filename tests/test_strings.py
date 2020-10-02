from algorithms.strings import (
    add_binary,
    match_symbol, match_symbol_1, bracket,
    decode_string,
    delete_reoccurring_characters,
    domain_name_1, domain_name_2,
    encode, decode,
    group_anagrams,
    int_to_roman,
    is_palindrome, is_palindrome_reverse,
    is_palindrome_two_pointer, is_palindrome_stack,
    is_rotated, is_rotated_v1,
    license_number,
    make_sentence,
    is_merge_recursive, is_merge_iterative,
    multiply,
    is_one_edit, is_one_edit2,
    rabin_karp,
    ultra_pythonic, iterative, recursive, pythonic,
    reverse_vowel,
    reverse_words,
    roman_to_int,
    strip_url_params1, strip_url_params2, strip_url_params3,
    is_valid_coordinates_0, is_valid_coordinates_1,
    is_valid_coordinates_regular_expression,
    word_squares,
    convert_morse_word, unique_morse,
    judge_circle,
    strong_password,
    caesar_cipher,
    check_pangram,
    contain_string,
    count_binary_substring,
    repeat_string,
    text_justification,
    min_distance,
    longest_common_prefix_v1, longest_common_prefix_v2, longest_common_prefix_v3,
    rotate,
    first_unique_char,
    repeat_substring,
    atbash,
    longest_palindrome,
    knuth_morris_pratt
)

import unittest


class TestAddBinary(unittest.TestCase):
    """[summary]
    Test for the file add_binary.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_add_binary(self):
        self.assertEqual("100", add_binary("11", "1"))
        self.assertEqual("101", add_binary("100", "1"))
        self.assertEqual("10", add_binary("1", "1"))


class TestBreakingBad(unittest.TestCase):
    """[summary]
    Test for the file breaking_bad.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def setUp(self):
        self.words = ['Amazon', 'Microsoft', 'Google']
        self.symbols = ['i', 'Am', 'cro', 'le', 'abc']
        self.result = ['M[i]crosoft', '[Am]azon', 'Mi[cro]soft', 'Goog[le]']

    def test_match_symbol(self):
        self.assertEqual(self.result, match_symbol(self.words, self.symbols))

    def test_match_symbol_1(self):
        self.assertEqual(['[Am]azon', 'Mi[cro]soft', 'Goog[le]'], match_symbol_1(self.words, self.symbols))

    def test_bracket(self):
        self.assertEqual(('[Am]azon', 'Mi[cro]soft', 'Goog[le]'), bracket(self.words, self.symbols))
        self.assertEqual(('Amazon', 'Microsoft', 'Google'), bracket(self.words, ['thisshouldnotmatch']))
        self.assertEqual(('Amazon', 'M[i]crosoft', 'Google'), bracket(self.words, ['i', 'i']))

class TestDecodeString(unittest.TestCase):
    """[summary]
    Test for the file decode_string.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_decode_string(self):
        self.assertEqual("aaabcbc", decode_string("3[a]2[bc]"))
        self.assertEqual("accaccacc", decode_string("3[a2[c]]"))


class TestDeleteReoccurring(unittest.TestCase):
    """[summary]
    Test for the file delete_reoccurring.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_delete_reoccurring_characters(self):
        self.assertEqual("abc", delete_reoccurring_characters("aaabcccc"))


class TestDomainExtractor(unittest.TestCase):
    """[summary]
    Test for the file domain_extractor.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_valid(self):
        self.assertEqual(domain_name_1("https://github.com/SaadBenn"), "github")

    def test_invalid(self):
        self.assertEqual(domain_name_2("http://google.com"), "google")


class TestEncodeDecode(unittest.TestCase):
    """[summary]
    Test for the file encode_decode.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_encode(self):
        self.assertEqual("4:keon2:is7:awesome", encode("keon is awesome"))

    def test_decode(self):
        self.assertEqual(['keon', 'is', 'awesome'], decode("4:keon2:is7:awesome"))


class TestGroupAnagrams(unittest.TestCase):
    """[summary]
    Test for the file group_anagrams.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_group_anagrams(self):
        self.assertEqual([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']], \
                         group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


class TestIntToRoman(unittest.TestCase):
    """[summary]
    Test for the file int_to_roman.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_int_to_roman(self):
        self.assertEqual("DCXLIV", int_to_roman(644))
        self.assertEqual("I", int_to_roman(1))
        self.assertEqual("MMMCMXCIX", int_to_roman(3999))


class TestIsPalindrome(unittest.TestCase):
    """[summary]
    Test for the file is_palindrome.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_is_palindrome(self):
        # 'Otto' is a old german name.
        self.assertTrue(is_palindrome("Otto"))
        self.assertFalse(is_palindrome("house"))

    def test_is_palindrome_reverse(self):
        # 'Otto' is a old german name.
        self.assertTrue(is_palindrome_reverse("Otto"))
        self.assertFalse(is_palindrome_reverse("house"))

    def test_is_palindrome_two_pointer(self):
        # 'Otto' is a old german name.
        self.assertTrue(is_palindrome_two_pointer("Otto"))
        self.assertFalse(is_palindrome_two_pointer("house"))

    def test_is_palindrome_stack(self):
        # 'Otto' is a old german name.
        self.assertTrue(is_palindrome_stack("Otto"))
        self.assertFalse(is_palindrome_stack("house"))


class TestIsRotated(unittest.TestCase):
    """[summary]
    Test for the file is_rotated.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_is_rotated(self):
        self.assertTrue(is_rotated("hello", "hello"))
        self.assertTrue(is_rotated("hello", "llohe"))
        self.assertFalse(is_rotated("hello", "helol"))
        self.assertFalse(is_rotated("hello", "lloh"))
        self.assertTrue(is_rotated("", ""))

    def test_is_rotated_v1(self):
        self.assertTrue(is_rotated_v1("hello", "hello"))
        self.assertTrue(is_rotated_v1("hello", "llohe"))
        self.assertFalse(is_rotated_v1("hello", "helol"))
        self.assertFalse(is_rotated_v1("hello", "lloh"))
        self.assertTrue(is_rotated_v1("", ""))


class TestRotated(unittest.TestCase):
    def test_rotate(self):
        self.assertEqual("llohe", rotate("hello", 2))
        self.assertEqual("hello", rotate("hello", 5))
        self.assertEqual("elloh", rotate("hello", 6))
        self.assertEqual("llohe", rotate("hello", 7))


class TestLicenseNumber(unittest.TestCase):
    """[summary]
    Test for the file license_number.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_license_number(self):
        self.assertEqual("a-b-c-d-f-d-d-f", license_number("a-bc-dfd-df", 1))
        self.assertEqual("ab-cd-fd-df", license_number("a-bc-dfd-df", 2))
        self.assertEqual("ab-cdf-ddf", license_number("a-bc-dfd-df", 3))
        self.assertEqual("abcd-fddf", license_number("a-bc-dfd-df", 4))
        self.assertEqual("abc-dfddf", license_number("a-bc-dfd-df", 5))


class TestMakeSentence(unittest.TestCase):
    """[summary]
    Test for the file make_sentence.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_make_sentence(self):
        dictionarys = ["", "app", "let", "t", "apple", "applet"]
        word = "applet"
        self.assertTrue(make_sentence(word, dictionarys))


class TestMergeStringChecker(unittest.TestCase):
    """[summary]
    Test for the file merge_string_checker.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_is_merge_recursive(self):
        self.assertTrue(is_merge_recursive("codewars", "cdw", "oears"))

    def test_is_merge_iterative(self):
        self.assertTrue(is_merge_iterative("codewars", "cdw", "oears"))


class TestMultiplyStrings(unittest.TestCase):
    """[summary]
    Test for the file multiply_strings.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_multiply(self):
        self.assertEqual("23", multiply("1", "23"))
        self.assertEqual("529", multiply("23", "23"))
        self.assertEqual("0", multiply("0", "23"))
        self.assertEqual("1000000", multiply("100", "10000"))


class TestOneEditDistance(unittest.TestCase):
    """[summary]
    Test for the file one_edit_distance.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_is_one_edit(self):
        self.assertTrue(is_one_edit("abc", "abd"))
        self.assertFalse(is_one_edit("abc", "aed"))
        self.assertFalse(is_one_edit("abcd", "abcd"))

    def test_is_one_edit2(self):
        self.assertTrue(is_one_edit2("abc", "abd"))
        self.assertFalse(is_one_edit2("abc", "aed"))
        self.assertFalse(is_one_edit2("abcd", "abcd"))


class TestRabinKarp(unittest.TestCase):
    """[summary]
    Test for the file rabin_karp.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_rabin_karp(self):
        self.assertEqual(3, rabin_karp("abc", "zsnabckfkd"))
        self.assertEqual(None, rabin_karp("abc", "zsnajkskfkd"))


class TestReverseString(unittest.TestCase):
    """[summary]
    Test for the file reverse_string.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_recursive(self):
        self.assertEqual("ereht olleh", recursive("hello there"))

    def test_iterative(self):
        self.assertEqual("ereht olleh", iterative("hello there"))

    def test_pythonic(self):
        self.assertEqual("ereht olleh", pythonic("hello there"))

    def test_ultra_pythonic(self):
        self.assertEqual("ereht olleh", ultra_pythonic("hello there"))


class TestReverseVowel(unittest.TestCase):
    """[summary]
    Test for the file reverse_vowel.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_reverse_vowel(self):
        self.assertEqual("holle", reverse_vowel("hello"))


class TestReverseWords(unittest.TestCase):
    """[summary]
    Test for the file reverse_words.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_reverse_words(self):
        self.assertEqual("pizza like I and kim keon am I", \
                         reverse_words("I am keon kim and I like pizza"))


class TestRomanToInt(unittest.TestCase):
    """[summary]
    Test for the file roman_to_int.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_roman_to_int(self):
        self.assertEqual(621, roman_to_int("DCXXI"))
        self.assertEqual(1, roman_to_int("I"))
        self.assertEqual(3999, roman_to_int("MMMCMXCIX"))


# class TestStripUrlParams(unittest.TestCase):
#     """[summary]
#     Test for the file strip_urls_params.py

#     Arguments:
#         unittest {[type]} -- [description]
#     """

#     def test_strip_url_params1(self):
#         self.assertEqual(strip_url_params1("www.saadbenn.com?a=1&b=2&a=2"), "www.saadbenn.com?a=1&b=2")
#         self.assertEqual(strip_url_params1("www.saadbenn.com?a=1&b=2", ['b']), "www.saadbenn.com?a=1")
#     def test_strip_url_params2(self):
#         self.assertEqual(strip_url_params2("www.saadbenn.com?a=1&b=2&a=2"), "www.saadbenn.com?a=1&b=2")
#         self.assertEqual(strip_url_params2("www.saadbenn.com?a=1&b=2", ['b']), "www.saadbenn.com?a=1")
#     def test_strip_url_params3(self):
#         self.assertEqual(strip_url_params3("www.saadbenn.com?a=1&b=2&a=2"), "www.saadbenn.com?a=1&b=2")
#         self.assertEqual(strip_url_params3("www.saadbenn.com?a=1&b=2", ['b']), "www.saadbenn.com?a=1")


class TestValidateCoordinates(unittest.TestCase):
    """[summary]
    Test for the file validate_coordinates.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_valid(self):
        valid_coordinates = ["-23, 25", "4, -3", "90, 180", "-90, -180"]
        for coordinate in valid_coordinates:
            self.assertTrue(is_valid_coordinates_0(coordinate))

    def test_invalid(self):
        invalid_coordinates = ["23.234, - 23.4234", "99.234, 12.324", "6.325624, 43.34345.345", "0, 1,2", "23.245, 1e1"]
        for coordinate in invalid_coordinates:
            self.assertFalse(is_valid_coordinates_0(coordinate))


class TestWordSquares(unittest.TestCase):
    """[summary]
    Test for the file word_squares.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_word_squares(self):
        self.assertEqual([['wall', 'area', 'lead', 'lady'], ['ball', 'area', 'lead', 'lady']], \
                         word_squares(["area", "lead", "wall", "lady", "ball"]))


class TestUniqueMorse(unittest.TestCase):
    def test_convert_morse_word(self):
        self.assertEqual("--...-.", convert_morse_word("gin"))
        self.assertEqual("--...--.", convert_morse_word("msg"))

    def test_unique_morse(self):
        self.assertEqual(2, unique_morse(["gin", "zen", "gig", "msg"]))


class TestJudgeCircle(unittest.TestCase):
    def test_judge_circle(self):
        self.assertTrue(judge_circle("UDLRUD"))
        self.assertFalse(judge_circle("LLRU"))


class TestStrongPassword(unittest.TestCase):
    def test_strong_password(self):
        self.assertEqual(3, strong_password(3, "Ab1"))
        self.assertEqual(1, strong_password(11, "#Algorithms"))


class TestCaesarCipher(unittest.TestCase):
    def test_caesar_cipher(self):
        self.assertEqual("Lipps_Asvph!", caesar_cipher("Hello_World!", 4))
        self.assertEqual("okffng-Qwvb", caesar_cipher("middle-Outz", 2))

class TestCheckPangram(unittest.TestCase):
    def test_check_pangram(self):
        self.assertTrue(check_pangram("The quick brown fox jumps over the lazy dog"))
        self.assertFalse(check_pangram("The quick brown fox"))


class TestContainString(unittest.TestCase):
    def test_contain_string(self):
        self.assertEqual(-1, contain_string("mississippi", "issipi"))
        self.assertEqual(0, contain_string("Hello World", ""))
        self.assertEqual(2, contain_string("hello", "ll"))


class TestCountBinarySubstring(unittest.TestCase):
    def test_count_binary_substring(self):
        self.assertEqual(6, count_binary_substring("00110011"))
        self.assertEqual(4, count_binary_substring("10101"))
        self.assertEqual(3, count_binary_substring("00110"))


class TestCountBinarySubstring(unittest.TestCase):
    def test_repeat_string(self):
        self.assertEqual(3, repeat_string("abcd", "cdabcdab"))
        self.assertEqual(4, repeat_string("bb", "bbbbbbb"))


class TestTextJustification(unittest.TestCase):
    def test_text_justification(self):
        self.assertEqual(["This    is    an",
                          "example  of text",
                          "justification.  "],

                         text_justification(["This", "is", "an", "example", "of", "text", "justification."]
                                            , 16)
                         )

        self.assertEqual(["What   must   be",
                          "acknowledgment  ",
                          "shall be        "],

                         text_justification(["What", "must", "be", "acknowledgment", "shall", "be"]
                                            , 16)
                         )

class TestMinDistance(unittest.TestCase):
    def test_min_distance(self):
        self.assertEqual(2, min_distance("sea", "eat"))
        self.assertEqual(6, min_distance("abAlgocrithmf", "Algorithmmd"))

class TestLongestCommonPrefix(unittest.TestCase):
    def test_longest_common_prefix(self):
        # Test first solution
        self.assertEqual("fl", longest_common_prefix_v1(["flower","flow","flight"]))
        self.assertEqual("", longest_common_prefix_v1(["dog","racecar","car"]))
        # Test second solution
        self.assertEqual("fl", longest_common_prefix_v2(["flower","flow","flight"]))
        self.assertEqual("", longest_common_prefix_v2(["dog","racecar","car"]))
        # Test third solution
        self.assertEqual("fl", longest_common_prefix_v3(["flower","flow","flight"]))
        self.assertEqual("", longest_common_prefix_v3(["dog","racecar","car"]))

class TestFirstUniqueChar(unittest.TestCase):
    def test_first_unique_char(self):
        self.assertEqual(0, first_unique_char("leetcode"))
        self.assertEqual(2, first_unique_char("loveleetcode"))

class TestRepeatSubstring(unittest.TestCase):
    def test_repeat_substring(self):
        self.assertTrue(repeat_substring("abab"))
        self.assertFalse(repeat_substring("aba"))
        self.assertTrue(repeat_substring("abcabcabcabc"))

class TestAtbashCipher(unittest.TestCase):
    """[summary]
    Test for the file atbash_cipher.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_atbash_cipher(self):
        self.assertEqual("zyxwvutsrqponml", atbash("abcdefghijklmno"))
        self.assertEqual("KbgslM", atbash("PythoN"))
        self.assertEqual("AttaCK at DawN", atbash("ZggzXP zg WzdM"))
        self.assertEqual("ZggzXP zg WzdM", atbash("AttaCK at DawN"))



class TestLongestPalindromicSubstring(unittest.TestCase):
    """[summary]
    Test for the file longest_palindromic_substring.py
    
    Arguments:
        unittest {[type]} -- [description]
    """
    
    def test_longest_palindromic_substring(self):
        self.assertEqual("bb", longest_palindrome("cbbd"))
        self.assertEqual("abba", longest_palindrome("abba"))
        self.assertEqual("asdadsa", longest_palindrome("dasdasdasdasdasdadsa"))
        self.assertEqual("abba", longest_palindrome("cabba"))

        
class TestKnuthMorrisPratt(unittest.TestCase):
    """[summary]
    Test for the file knuth_morris_pratt.py


    Arguments:
        unittest {[type]} -- [description]
    """

    def test_knuth_morris_pratt(self):
        self.assertEqual([0, 1, 2, 3, 4], knuth_morris_pratt("aaaaaaa", "aaa"))
        self.assertEqual([0, 4], knuth_morris_pratt("abcdabc", "abc"))
        self.assertEqual([], knuth_morris_pratt("aabcdaab", "aba"))


if __name__ == "__main__":
    unittest.main()
