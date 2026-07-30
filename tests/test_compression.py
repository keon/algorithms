import unittest

from algorithms.compression.elias import elias_delta, elias_gamma
from algorithms.compression.huffman_coding import HuffmanCoding
from algorithms.compression.lzw_compression import lzw_decode, lzw_encode
from algorithms.compression.rle_compression import decode_rle, encode_rle


class TestHuffmanCoding(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_in_name = "huffman_coding_in.txt"
        cls.file_out_bin_name = "huffman_coding_out.bin"
        cls.file_out_name = "huffman_coding_out.txt"

    def setUp(self):
        import random

        random.seed(1951)
        with open(self.file_in_name, "wb") as file_in:
            for _ in range(10000):
                file_in.write(bytes([random.randrange(0, 256)]))

    def test_huffman_coding(self):
        HuffmanCoding.encode_file(self.file_in_name, self.file_out_bin_name)
        HuffmanCoding.decode_file(self.file_out_bin_name, self.file_out_name)

        with (
            open(self.file_in_name, "rb") as file_1,
            open(self.file_out_name, "rb") as file_2,
        ):
            content_1 = file_1.read()
            content_2 = file_2.read()

            self.assertEqual(content_1, content_2)

    def tearDown(self):
        import os

        os.remove(self.file_in_name)
        os.remove(self.file_out_bin_name)
        os.remove(self.file_out_name)


class TestRLECompression(unittest.TestCase):
    def test_encode_rle(self):
        self.assertEqual(
            "12W1B12W3B24W1B14W",
            encode_rle(
                "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
            ),
        )

    def test_decode_rle(self):
        self.assertEqual(
            "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
            decode_rle("12W1B12W3B24W1B14W"),
        )


class TestEliasCoding(unittest.TestCase):
    def test_elias_gamma(self):
        correct_result = [
            "1",
            "010",
            "011",
            "00100",
            "00101",
            "00110",
            "00111",
            "0001000",
            "0001001",
            "0001010",
        ]

        result = [elias_gamma(i) for i in range(1, 11)]

        self.assertEqual(correct_result, result)
        with self.assertRaises(ValueError):
            elias_gamma(0)

    def test_elias_delta(self):
        correct_result = [
            "1",
            "0100",
            "0101",
            "01100",
            "01101",
            "01110",
            "01111",
            "00100000",
            "00100001",
            "00100010",
        ]

        result = [elias_delta(i) for i in range(1, 11)]

        self.assertEqual(correct_result, result)
        with self.assertRaises(ValueError):
            elias_delta(0)


class TestLZWCompression(unittest.TestCase):
    def test_lzw_encode(self):
        codes, dictionary = lzw_encode("ABABABA")
        self.assertEqual([0, 1, 2, 4], codes)
        self.assertEqual({0: "A", 1: "B"}, dictionary)

    def test_lzw_decode(self):
        self.assertEqual("ABABABA", lzw_decode([0, 1, 2, 4], {0: "A", 1: "B"}))

    def test_lzw_roundtrip(self):
        data = "TOBEORNOTTOBEORTOBEORNOT"
        encoded, dictionary = lzw_encode(data)
        decoded = lzw_decode(encoded, dictionary)
        self.assertEqual(data, decoded)

    def test_lzw_empty(self):
        self.assertEqual(([], {}), lzw_encode(""))
        self.assertEqual("", lzw_decode([], {}))


if __name__ == "__main__":
    unittest.main()
