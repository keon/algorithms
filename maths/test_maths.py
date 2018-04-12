from base_conversion import int2base,base2int
from extended_gcd import extended_gcd
from gcd import gcd,lcm
from generate_strobogrammtic import gen_strobogrammatic,strobogrammaticInRange
from is_strobogrammatic import is_strobogrammatic,is_strobogrammatic2
from next_perfect_square import find_next_square,find_next_square2
from primes_sieve_of_eratosthenes import primes
from prime_test import prime_test, prime_test2
from pythagoras import pythagoras
from rabin_miller import is_prime 
from rsa import encrypt, decrypt, generate_key

import unittest


class TestBaseConversion(unittest.TestCase):
    """
    Test for the file base_conversion.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_int2base(self):
        self.assertEqual("101",int2base(5,2))
        self.assertEqual("0",int2base(0,2))
        self.assertEqual("FF",int2base(255,16))
    def test_base2int(self):
        self.assertEqual(5,base2int("101",2))
        self.assertEqual(0,base2int("0",2))
        self.assertEqual(255,base2int("FF",16))


class TestExtendedGcd(unittest.TestCase):
    """[summary]
    Test for the file extended_gcd.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_extended_gcd(self):
        self.assertEqual((0,1,2),extended_gcd(8,2))
        self.assertEqual((0,1,17),extended_gcd(13,17))


class TestGcd(unittest.TestCase):
    """[summary]
    Test for the file gcd.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_gcd(self):
        self.assertEqual(4,gcd(8,12))
        self.assertEqual(1,gcd(13,17))
    def test_lcm(self):
        self.assertEqual(24,lcm(8,12))


class TestGenerateStroboGrammatic(unittest.TestCase):
    """[summary]
    Test for the file generate_strobogrammatic.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_gen_strobomatic(self):
        self.assertEqual(['88', '11', '96', '69'],gen_strobogrammatic(2))
    def test_strobogrammaticInRange(self):
        self.assertEqual(4,strobogrammaticInRange("10","100"))


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
        self.assertEqual(36,find_next_square(25))
        self.assertEqual(1,find_next_square(0))
    def test_find_next_square2(self):
        self.assertEqual(36,find_next_square2(25))
        self.assertEqual(1,find_next_square2(0))


class TestPrimesSieveOfEratosthenes(unittest.TestCase):
    """[summary]
    Test for the file primes_sieve_of_eratosthenes.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_primes(self):
        self.assertEqual([2, 3, 5, 7],primes(7))


class TestPrimeTest (unittest.TestCase):
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
        for i in range(2,101):
            if prime_test(i):
                counter += 1
        self.assertEqual(25,counter)
    def test_prime_test2(self):
        """
            checks all prime numbers between 2 up to 100.
            Between 2 up to 100 exists 25 prime numbers!
        """
        counter = 0
        for i in range(2,101):
            if prime_test(i):
                counter += 1
        self.assertEqual(25,counter)
        

class TestPythagoras(unittest.TestCase):
    """[summary]
    Test for the file pythagoras.py 

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_pythagoras(self):
        self.assertEqual("Hypotenuse = 3.605551275463989",pythagoras(3, 2, "?"))


class TestRabinMiller(unittest.TestCase):
    """[summary]
    Test for the file rabin_miller.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_is_prime(self):
        self.assertTrue(is_prime(7,2))
        self.assertTrue(is_prime(13,11))
        self.assertFalse(is_prime(6,2))


class TestRSA(unittest.TestCase):
    """[summary]
    Test for the file rsa.py

    Arguments:
        unittest {[type]} -- [description]
    """
    def test_encrypt_decrypt(self):
        self.assertEqual(7,decrypt(encrypt(7, 23, 143), 47, 143))
    def test_key_generator(self):
        n, e, d = generate_key(8)
        data = 2
        en = encrypt(data, e, n)
        dec = decrypt(en, d, n)
        self.assertEqual(data,dec)

if __name__ == "__main__":
    unittest.main()