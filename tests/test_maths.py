from algorithms.maths import (
    int_to_base, base_to_int,
    decimal_to_binary_ip,
    euler_totient,
    extended_gcd,
    factorial, factorial_recur,
    gcd, lcm,
    gen_strobogrammatic, strobogrammatic_in_range,
    is_strobogrammatic, is_strobogrammatic2,
    modular_exponential,
    find_next_square, find_next_square2,
    prime_check,
    get_primes,
    pythagoras,
    is_prime,
    encrypt, decrypt,
    combination, combination_memo
)

import unittest


class TestBaseConversion(unittest.TestCase):
    """
    Test for the file base_conversion.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_int_to_base(self):
        self.assertEqual("101", int_to_base(5, 2))
        self.assertEqual("0", int_to_base(0, 2))
        self.assertEqual("FF", int_to_base(255, 16))

    def test_base_to_int(self):
        self.assertEqual(5, base_to_int("101", 2))
        self.assertEqual(0, base_to_int("0", 2))
        self.assertEqual(255, base_to_int("FF", 16))


class TestDecimalToBinaryIP(unittest.TestCase):
    """
    Test for the file decimal_to_binary_ip.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_decimal_to_binary_ip(self):
        self.assertEqual("00000000.00000000.00000000.00000000",
                         decimal_to_binary_ip("0.0.0.0"))
        self.assertEqual("11111111.11111111.11111111.11111111",
                         decimal_to_binary_ip("255.255.255.255"))
        self.assertEqual("11000000.10101000.00000000.00000001",
                         decimal_to_binary_ip("192.168.0.1"))


class TestEulerTotient(unittest.TestCase):
    """[summary]
    Test for the file euler_totient.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_euler_totient(self):
        self.assertEqual(4, euler_totient(8))
        self.assertEqual(12, euler_totient(21))
        self.assertEqual(311040, euler_totient(674614))
        self.assertEqual(2354352, euler_totient(3435145))


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


class TestModularExponential(unittest.TestCase):
    """[summary]
    Test for the file modular_Exponential.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_modular_exponential(self):
        self.assertEqual(1, modular_exponential(5, 117, 19))
        self.assertEqual(pow(1243, 65321, 10**9 + 7),
                         modular_exponential(1243, 65321, 10**9 + 7))
        self.assertEqual(1, modular_exponential(12, 0, 78))
        self.assertRaises(ValueError, modular_exponential, 12, -2, 455)


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
        self.assertListEqual([2, 3, 5, 7], get_primes(7))
        self.assertRaises(ValueError, get_primes, -42)


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

    def test_combination_memo(self):
        self.assertEqual(10272278170, combination_memo(50, 10))
        self.assertEqual(847660528, combination_memo(40, 10))


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
        self.assertEqual(637816310, factorial(34521, 10**9 + 7))
        self.assertRaises(ValueError, factorial, -42)
        self.assertRaises(ValueError, factorial, 42, -1)

    def test_factorial_recur(self):
        self.assertEqual(1, factorial_recur(0))
        self.assertEqual(120, factorial_recur(5))
        self.assertEqual(3628800, factorial_recur(10))
        self.assertEqual(637816310, factorial_recur(34521, 10**9 + 7))
        self.assertRaises(ValueError, factorial_recur, -42)
        self.assertRaises(ValueError, factorial_recur, 42, -1)


if __name__ == "__main__":
    unittest.main()
