from algorithms.compression.huffman_coding import HuffmanCoding
from algorithms.compression.rle_compression import (decode_rle, encode_rle)
from algorithms.compression.elias import (elias_gamma, elias_delta)

import unittest


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
            for i in range(10000):
                file_in.write(bytes([random.randrange(0, 256)]))

    def test_huffman_coding(self):
        HuffmanCoding.encode_file(self.file_in_name, self.file_out_bin_name)
        HuffmanCoding.decode_file(self.file_out_bin_name, self.file_out_name)

        with open(self.file_in_name, "rb") as file_1, open(self.file_out_name, "rb") as file_2:
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
        self.assertEqual('12W1B12W3B24W1B14W',
            encode_rle('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'))

    def test_decode_rle(self):
        self.assertEqual('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW', 
            decode_rle('12W1B12W3B24W1B14W'))

class TestEliasCoding(unittest.TestCase):

    def test_elias_gamma(self):
        correct_result = ['0', '00', '100', '101', '11000', '11001', '11010', '11011', '1110000', '1110001', '1110010']
        
        result = []
        for i in range(11):	
            result.append(elias_gamma(i))

        self.assertEqual(correct_result, result)

    def test_elias_delta(self):
        correct_result = ['0', '000', '1000', '1001', '10100', '10101', '10110', '10111', '11000000', '11000001', '11000010']

        result = []
        for i in range(11):	
            result.append(elias_delta(i))

        self.assertEqual(correct_result, result)        

if __name__ == "__main__":
    unittest.main()
