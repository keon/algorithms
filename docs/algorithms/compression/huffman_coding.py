"""
Huffman coding is an efficient method of compressing data without losing information.
This algorithm analyzes the symbols that appear in a message.
Symbols that appear more often will be encoded as a shorter-bit string
while symbols that aren't used as much will be encoded as longer strings.
"""

from collections import defaultdict, deque
import heapq


class Node:
    def __init__(self, frequency=0, sign=None, left=None, right=None):
        self.frequency = frequency
        self.sign = sign
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __str__(self):
        return "<ch: {0}: {1}>".format(self.sign, self.frequency)

    def __repr__(self):
        return "<ch: {0}: {1}>".format(self.sign, self.frequency)


class HuffmanReader:
    def __init__(self, file):
        self.file = file
        self.buffer = []
        self.is_last_byte = False

    def get_number_of_additional_bits_in_the_last_byte(self) -> int:
        bin_num = self.get_bit() + self.get_bit() + self.get_bit()
        return int(bin_num, 2)

    def load_tree(self) -> Node:
        """
        Load tree from file

        :return:
        """
        node_stack = deque()
        queue_leaves = deque()
        root = Node()

        current_node = root
        is_end_of_tree = False
        while not is_end_of_tree:
            current_bit = self.get_bit()
            if current_bit == "0":
                current_node.left = Node()
                current_node.right = Node()
                node_stack.append(current_node.right)  # going to left node, right push on stack
                current_node = current_node.left
            else:
                queue_leaves.append(current_node)
                if node_stack:
                    current_node = node_stack.pop()
                else:
                    is_end_of_tree = True

        self._fill_tree(queue_leaves)

        return root

    def _fill_tree(self, leaves_queue):
        """
        Load values to tree after reading tree
        :param leaves_queue:
        :return:
        """
        leaves_queue.reverse()
        while leaves_queue:
            node = leaves_queue.pop()
            s = int(self.get_byte(), 2)
            node.sign = s

    def _load_byte(self, buff_limit=8) -> bool:
        """
        Load next byte is buffer is less than buff_limit
        :param buff_limit:
        :return: True if there is enough bits in buffer to read
        """
        if len(self.buffer) <= buff_limit:
            byte = self.file.read(1)

            if not byte:
                return False

            i = int.from_bytes(byte, "big")
            self.buffer.extend(list("{0:08b}".format(i)))

        return True

    def get_bit(self, buff_limit=8):
        if self._load_byte(buff_limit):
            bit = self.buffer.pop(0)
            return bit
        else:
            return -1

    def get_byte(self):
        if self._load_byte():
            byte_list = self.buffer[:8]
            self.buffer = self.buffer[8:]

            return "".join(byte_list)
        else:
            return -1


class HuffmanWriter:
    def __init__(self, file):
        self.file = file
        self.buffer = ""
        self.saved_bits = 0

    def write_char(self, char):
        self.write_int(ord(char))

    def write_int(self, num):
        bin_int = "{0:08b}".format(num)
        self.write_bits(bin_int)

    def write_bits(self, bits):
        self.saved_bits += len(bits)

        self.buffer += bits

        while len(self.buffer) >= 8:
            i = int(self.buffer[:8], 2)
            self.file.write(bytes([i]))
            self.buffer = self.buffer[8:]

    def save_tree(self, tree):
        """
        Generate and save tree code to file
        :param tree:
        :return:
        """
        signs = []
        tree_code = ""

        def get_code_tree(T):
            nonlocal tree_code
            if T.sign is not None:
                signs.append(T.sign)
            if T.left:
                tree_code += "0"
                get_code_tree(T.left)
            if T.right:
                tree_code += "1"
                get_code_tree(T.right)

        get_code_tree(tree)
        self.write_bits(tree_code + "1")  # "1" indicates that tree ended (it will be needed to load the tree)
        for int_sign in signs:
            self.write_int(int_sign)

    def _save_information_about_additional_bits(self, additional_bits: int):
        """
        Overwrite first three bits in the file
        :param additional_bits: number of bits that were appended to fill last byte
        :return:
        """
        self.file.seek(0)
        first_byte_raw = self.file.read(1)
        self.file.seek(0)
        first_byte = "{0:08b}".format(int.from_bytes(first_byte_raw, "big"))
        # overwrite first three bits
        first_byte = first_byte[3:]
        first_byte = "{0:03b}".format(additional_bits) + first_byte

        self.write_bits(first_byte)

    def close(self):
        additional_bits = 8 - len(self.buffer)
        if additional_bits != 8:  # buffer is empty, no need to append extra "0"
            self.write_bits("0" * additional_bits)
            self._save_information_about_additional_bits(additional_bits)


class TreeFinder:
    """
    Class to help find signs in tree
    """

    def __init__(self, tree):
        self.root = tree
        self.current_node = tree
        self.found = None

    def find(self, bit):
        """
        Find sign in tree
        :param bit:
        :return: True if sign is found
        """
        if bit == "0":
            self.current_node = self.current_node.left
        elif bit == "1":
            self.current_node = self.current_node.right
        else:
            self._reset()
            return True

        if self.current_node.sign is not None:
            self._reset(self.current_node.sign)
            return True
        else:
            return False

    def _reset(self, found=""):
        self.found = found
        self.current_node = self.root


class HuffmanCoding:
    def __init__(self):
        pass

    @staticmethod
    def decode_file(file_in_name, file_out_name):
        with open(file_in_name, "rb") as file_in, open(file_out_name, "wb") as file_out:
            reader = HuffmanReader(file_in)
            additional_bits = reader.get_number_of_additional_bits_in_the_last_byte()
            tree = reader.load_tree()

            HuffmanCoding._decode_and_write_signs_to_file(file_out, reader, tree, additional_bits)

        print("File decoded.")

    @staticmethod
    def _decode_and_write_signs_to_file(file, reader: HuffmanReader, tree: Node, additional_bits: int):
        tree_finder = TreeFinder(tree)
        is_end_of_file = False

        while not is_end_of_file:
            bit = reader.get_bit()
            if bit != -1:
                while not tree_finder.find(bit):  # read whole code
                    bit = reader.get_bit(0)
                file.write(bytes([tree_finder.found]))
            else:  # There is last byte in buffer to parse
                is_end_of_file = True
                last_byte = reader.buffer
                last_byte = last_byte[:-additional_bits]  # remove additional "0" used to fill byte
                for bit in last_byte:
                    if tree_finder.find(bit):
                        file.write(bytes([tree_finder.found]))

    @staticmethod
    def encode_file(file_in_name, file_out_name):
        with open(file_in_name, "rb") as file_in, open(file_out_name, mode="wb+") as file_out:
            signs_frequency = HuffmanCoding._get_char_frequency(file_in)
            file_in.seek(0)
            tree = HuffmanCoding._create_tree(signs_frequency)
            codes = HuffmanCoding._generate_codes(tree)

            writer = HuffmanWriter(file_out)
            writer.write_bits("000")  # leave space to save how many bits will be appended to fill the last byte
            writer.save_tree(tree)
            HuffmanCoding._encode_and_write_signs_to_file(file_in, writer, codes)
            writer.close()

        print("File encoded.")

    @staticmethod
    def _encode_and_write_signs_to_file(file, writer: HuffmanWriter, codes: dict):
        sign = file.read(1)
        while sign:
            int_char = int.from_bytes(sign, "big")
            writer.write_bits(codes[int_char])
            sign = file.read(1)

    @staticmethod
    def _get_char_frequency(file) -> dict:
        is_end_of_file = False
        signs_frequency = defaultdict(lambda: 0)
        while not is_end_of_file:
            prev_pos = file.tell()
            sign = file.read(1)
            curr_pos = file.tell()
            if prev_pos == curr_pos:
                is_end_of_file = True
            else:
                signs_frequency[int.from_bytes(sign, "big")] += 1

        return signs_frequency

    @staticmethod
    def _generate_codes(tree: Node) -> dict:
        codes = dict()
        HuffmanCoding._go_through_tree_and_create_codes(tree, "", codes)
        return codes

    @staticmethod
    def _create_tree(signs_frequency: dict) -> Node:
        nodes = [Node(frequency=frequency, sign=char_int) for char_int, frequency in signs_frequency.items()]
        heapq.heapify(nodes)

        while len(nodes) > 1:
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)
            new_node = Node(frequency=left.frequency + right.frequency, left=left, right=right)
            heapq.heappush(nodes, new_node)

        return nodes[0]  # root

    @staticmethod
    def _go_through_tree_and_create_codes(tree: Node, code: str, dict_codes: dict):
        if tree.sign is not None:
            dict_codes[tree.sign] = code

        if tree.left:
            HuffmanCoding._go_through_tree_and_create_codes(tree.left, code + "0", dict_codes)

        if tree.right:
            HuffmanCoding._go_through_tree_and_create_codes(tree.right, code + "1", dict_codes)
