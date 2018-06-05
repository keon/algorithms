from algorithms.maths import (
    int2base, base2int,
    extended_gcd,
    factorial, factorial_recur,
    gcd, lcm,
    gen_strobogrammatic, strobogrammatic_in_range,
    is_strobogrammatic, is_strobogrammatic2,
    find_next_square, find_next_square2,
    prime_check, prime_check2,
    primes,
    pythagoras,
    is_prime,
    encrypt, decrypt, generate_key,
    combination
)

import unittest


class TestBaseConversion(unittest.TestCase):
    """
    Test for the file base_conversion.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_int2base(self):
        self.assertEqual("101", int2base(5, 2))
        self.assertEqual("0", int2base(0, 2))
        self.assertEqual("FF", int2base(255, 16))

    def test_base2int(self):
        self.assertEqual(5, base2int("101", 2))
        self.assertEqual(0, base2int("0", 2))
        self.assertEqual(255, base2int("FF", 16))


class TestExtendedGcd(unittest.TestCase):
    """[summary]
    Test for the file extended_gcd.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_extended_gcd(self):
        self.assertEqual((0, 1, 2), extended_gcd(8, 2))
        self.assertEqual((0, 1, 17), extended_gcd(13, 17))


class TestGcd(unittest.TestCase):
    """[summary]
    Test for the file gcd.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_gcd(self):
        self.assertEqual(4, gcd(8, 12))
        self.assertEqual(1, gcd(13, 17))

    def test_lcm(self):
        self.assertEqual(24, lcm(8, 12))


class TestGenerateStroboGrammatic(unittest.TestCase):
    """[summary]
    Test for the file generate_strobogrammatic.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_gen_strobomatic(self):
        self.assertEqual(['88', '11', '96', '69'], gen_strobogrammatic(2))

    def test_strobogrammatic_in_range(self):
        self.assertEqual(4, strobogrammatic_in_range("10", "100"))


class TestIsStrobogrammatic(unittest.TestCase):
    """[summary]
    Test for the file is_strobogrammatic.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_is_strobogrammatic(self):
        self.assertTrue(is_strobogrammatic("69"))
        self.assertFalse(is_strobogrammatic("14"))

    def test_is_strobogrammatic2(self):
        self.assertTrue(is_strobogrammatic2("69"))
        self.assertFalse(is_strobogrammatic2("14"))


class TestNextPerfectSquare(unittest.TestCase):
    """[summary]
    Test for the file next_perfect_square.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_find_next_square(self):
        self.assertEqual(36, find_next_square(25))
        self.assertEqual(1, find_next_square(0))

    def test_find_next_square2(self):
        self.assertEqual(36, find_next_square2(25))
        self.assertEqual(1, find_next_square2(0))


class TestPrimesSieveOfEratosthenes(unittest.TestCase):
    """[summary]
    Test for the file primes_sieve_of_eratosthenes.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_primes(self):
        self.assertEqual([2, 3, 5, 7], primes(7))


class TestPrimeTest(unittest.TestCase):
    """[summary]
    Test for the file prime_test.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_prime_test(self):
        """
            checks all prime numbers between 2 up to 100.
            Between 2 up to 100 exists 25 prime numbers!
        """
        counter = 0
        for i in range(2, 101):
            if prime_check(i):
                counter += 1
        self.assertEqual(25, counter)

    def test_prime_test2(self):
        """
            checks all prime numbers between 2 up to 100.
            Between 2 up to 100 exists 25 prime numbers!
        """
        counter = 0
        for i in range(2, 101):
            if prime_check2(i):
                counter += 1
        self.assertEqual(25, counter)


class TestPythagoras(unittest.TestCase):
    """[summary]
    Test for the file pythagoras.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_pythagoras(self):
        self.assertEqual("Hypotenuse = 3.605551275463989", pythagoras(3, 2, "?"))


class TestRabinMiller(unittest.TestCase):
    """[summary]
    Test for the file rabin_miller.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_is_prime(self):
        self.assertTrue(is_prime(7, 2))
        self.assertTrue(is_prime(13, 11))
        self.assertFalse(is_prime(6, 2))


class TestRSA(unittest.TestCase):
    """[summary]
    Test for the file rsa.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_encrypt_decrypt(self):

        self.assertEqual(7, decrypt(encrypt(7, 23, 143), 47, 143))

    # def test_key_generator(self):  # this test takes a while!
    #     for i in range(100):
    #         print("step {0}".format(i))
    #         n, e, d = generate_key(26)
    #         data = 2
    #         en = encrypt(data, e, n)
    #         dec = decrypt(en, d, n)
    #         self.assertEqual(data,dec)

class TestCombination(unittest.TestCase):
    """[summary]
    Test for the file combination.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_combination(self):
        self.assertEqual(10, combination(5, 2))
        self.assertEqual(252, combination(10, 5))
        
class TestFactorial(unittest.TestCase):
    """[summary]
    Test for the file factorial.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_factorial(self):
        self.assertEqual(1, factorial(0))
        self.assertEqual(120, factorial(5))
        self.assertEqual(3628800, factorial(10))
        
    def test_factorial_recur(self):
        self.assertEqual(1, factorial_recur(0))
        self.assertEqual(120, factorial_recur(5))
        self.assertEqual(3628800, factorial_recur(10))
        
if __name__ == "__main__":
    unittest.main()
    
    
