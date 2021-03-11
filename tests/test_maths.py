from algorithms.maths import (
    power, power_recur,
    int_to_base, base_to_int,
    decimal_to_binary_ip,
    euler_totient,
    extended_gcd,
    factorial, factorial_recur,
    gcd, lcm, trailing_zero, gcd_bit,
    gen_strobogrammatic, strobogrammatic_in_range,
    is_strobogrammatic, is_strobogrammatic2,
    modular_inverse,
    modular_exponential,
    find_next_square, find_next_square2,
    prime_check,
    get_primes,
    pythagoras,
    is_prime,
    encrypt, decrypt,
    combination, combination_memo,
    hailstone,
    cosine_similarity,
    magic_number,
    find_order,
    find_primitive_root,
    alice_private_key, alice_public_key, bob_private_key, bob_public_key, alice_shared_key, bob_shared_key, diffie_hellman_key_exchange,
    num_digits,
    alice_private_key, alice_public_key, bob_private_key, bob_public_key, alice_shared_key, bob_shared_key,
    diffie_hellman_key_exchange, krishnamurthy_number,
    chinese_remainder_theorem,
)

import unittest
import pytest


class TestPower(unittest.TestCase):
    """
    Test for the file power.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_power(self):
        self.assertEqual(8, power(2, 3))
        self.assertEqual(1, power(5, 0))
        self.assertEqual(0, power(10, 3, 5))
        self.assertEqual(280380, power(2265, 1664, 465465))

    def test_power_recur(self):
        self.assertEqual(8, power_recur(2, 3))
        self.assertEqual(1, power_recur(5, 0))
        self.assertEqual(0, power_recur(10, 3, 5))
        self.assertEqual(280380, power_recur(2265, 1664, 465465))


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

    def test_gcd_non_integer_input(self):
        with pytest.raises(ValueError, match=r"Input arguments are not integers"):
            gcd(1.0, 5)
            gcd(5, 6.7)
            gcd(33.8649, 6.12312312)

    def test_gcd_zero_input(self):
        with pytest.raises(ValueError, match=r"One or more input arguments equals zero"):
            gcd(0, 12)
            gcd(12, 0)
            gcd(0, 0)

    def test_gcd_negative_input(self):
        self.assertEqual(1, gcd(-13, -17))
        self.assertEqual(4, gcd(-8, 12))
        self.assertEqual(8, gcd(24, -16))

    def test_lcm(self):
        self.assertEqual(24, lcm(8, 12))
        self.assertEqual(5767, lcm(73, 79))

    def test_lcm_negative_numbers(self):
        self.assertEqual(24, lcm(-8, -12))
        self.assertEqual(5767, lcm(73, -79))
        self.assertEqual(1, lcm(-1, 1))

    def test_lcm_zero_input(self):
        with pytest.raises(ValueError, match=r"One or more input arguments equals zero"):
            lcm(0, 12)
            lcm(12, 0)
            lcm(0, 0)

    def test_trailing_zero(self):
        self.assertEqual(1, trailing_zero(34))
        self.assertEqual(3, trailing_zero(40))

    def test_gcd_bit(self):
        self.assertEqual(4, gcd_bit(8, 12))
        self.assertEqual(1, gcd(13, 17))



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


class TestModularInverse(unittest.TestCase):
    """[summary]
    Test for the file modular_Exponential.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_modular_inverse(self):
        # checks if x * x_inv == 1 (mod m)
        self.assertEqual(1, 2 * modular_inverse.modular_inverse(2, 19) % 19)
        self.assertEqual(1, 53 * modular_inverse.modular_inverse(53, 91) % 91)
        self.assertEqual(1, 2 * modular_inverse.modular_inverse(2, 1000000007) % 1000000007)
        self.assertRaises(ValueError, modular_inverse.modular_inverse, 2, 20)


class TestModularExponential(unittest.TestCase):
    """[summary]
    Test for the file modular_Exponential.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_modular_exponential(self):
        self.assertEqual(1, modular_exponential(5, 117, 19))
        self.assertEqual(pow(1243, 65321, 10 ** 9 + 7),
                         modular_exponential(1243, 65321, 10 ** 9 + 7))
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
        self.assertEqual(637816310, factorial(34521, 10 ** 9 + 7))
        self.assertRaises(ValueError, factorial, -42)
        self.assertRaises(ValueError, factorial, 42, -1)

    def test_factorial_recur(self):
        self.assertEqual(1, factorial_recur(0))
        self.assertEqual(120, factorial_recur(5))
        self.assertEqual(3628800, factorial_recur(10))
        self.assertEqual(637816310, factorial_recur(34521, 10 ** 9 + 7))
        self.assertRaises(ValueError, factorial_recur, -42)
        self.assertRaises(ValueError, factorial_recur, 42, -1)


class TestHailstone(unittest.TestCase):
    """[summary]
    Test for the file hailstone.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_hailstone(self):
        self.assertEqual([8, 4, 2, 1], hailstone.hailstone(8))
        self.assertEqual([10, 5, 16, 8, 4, 2, 1], hailstone.hailstone(10))


class TestCosineSimilarity(unittest.TestCase):
    """[summary]
    Test for the file cosine_similarity.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_cosine_similarity(self):
        vec_a = [1, 1, 1]
        vec_b = [-1, -1, -1]
        vec_c = [1, 2, -1]
        self.assertAlmostEqual(cosine_similarity(vec_a, vec_a), 1)
        self.assertAlmostEqual(cosine_similarity(vec_a, vec_b), -1)
        self.assertAlmostEqual(cosine_similarity(vec_a, vec_c), 0.4714045208)


class TestFindPrimitiveRoot(unittest.TestCase):
    """[summary]
    Test for the file find_primitive_root_simple.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_find_primitive_root_simple(self):
        self.assertListEqual([0], find_primitive_root(1))
        self.assertListEqual([2, 3], find_primitive_root(5))
        self.assertListEqual([], find_primitive_root(24))
        self.assertListEqual([2, 5, 13, 15, 17, 18, 19, 20, 22, 24, 32, 35], find_primitive_root(37))


class TestFindOrder(unittest.TestCase):
    """[summary]
    Test for the file find_order_simple.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_find_order_simple(self):
        self.assertEqual(1, find_order(1, 1))
        self.assertEqual(6, find_order(3, 7))
        self.assertEqual(-1, find_order(128, 256))
        self.assertEqual(352, find_order(3, 353))

class TestKrishnamurthyNumber(unittest.TestCase):
    """[summary]
    Test for the file krishnamurthy_number.py

    Arguments:
        unittest {[type]} -- [description]
    """
    
    def test_krishnamurthy_number(self):
        self.assertFalse(krishnamurthy_number(0))
        self.assertTrue(krishnamurthy_number(2))
        self.assertTrue(krishnamurthy_number(1))
        self.assertTrue(krishnamurthy_number(145))
        self.assertTrue(krishnamurthy_number(40585))


class TestMagicNumber(unittest.TestCase):
    """[summary]
    Test for the file find_order_simple.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_magic_number(self):
        self.assertTrue(magic_number(50113))
        self.assertTrue(magic_number(1234))
        self.assertTrue(magic_number(100))
        self.assertTrue(magic_number(199))
        self.assertFalse(magic_number(2000))
        self.assertFalse(magic_number(500000))


class TestDiffieHellmanKeyExchange(unittest.TestCase):
    """[summary]
    Test for the file diffie_hellman_key_exchange.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_find_order_simple(self):
        self.assertFalse(diffie_hellman_key_exchange(3, 6))
        self.assertTrue(diffie_hellman_key_exchange(3, 353))
        self.assertFalse(diffie_hellman_key_exchange(5, 211))
        self.assertTrue(diffie_hellman_key_exchange(11, 971))


class TestNumberOfDigits(unittest.TestCase):
    """[summary]
    Test for the file num_digits.py

    Arguments:
        unittest {[type]} -- [description]
    """
    def test_num_digits(self):
        self.assertEqual(2,num_digits(12))
        self.assertEqual(5,num_digits(99999))
        self.assertEqual(1,num_digits(8))
        self.assertEqual(1,num_digits(0))        
        self.assertEqual(1,num_digits(-5))
        self.assertEqual(3,num_digits(-254))

class TestChineseRemainderSolver(unittest.TestCase):
    def test_k_three(self):
        # Example which should give the answer 143
        # which is the smallest possible x that
        # solves the system of equations
        num = [3, 7, 10]
        rem = [2, 3, 3]
        self.assertEqual(chinese_remainder_theorem.solve_chinese_remainder(num, rem), 143)

    def test_k_five(self):
        # Example which should give the answer 3383
        # which is the smallest possible x that
        # solves the system of equations
        num = [3, 5, 7, 11, 26]
        rem = [2, 3, 2, 6, 3]
        self.assertEqual(chinese_remainder_theorem.solve_chinese_remainder(num, rem), 3383)

    def test_exception_non_coprime(self):
        # There should be an exception when all
        # numbers in num are not pairwise coprime
        num = [3, 7, 10, 14]
        rem = [2, 3, 3, 1]
        with self.assertRaises(Exception):
            chinese_remainder_theorem.solve_chinese_remainder(num, rem)

    def test_empty_lists(self):
        num = []
        rem = []
        with self.assertRaises(Exception):
            chinese_remainder_theorem.solve_chinese_remainder(num, rem)

if __name__ == "__main__":
    unittest.main()
