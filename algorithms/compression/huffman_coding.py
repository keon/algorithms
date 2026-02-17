"""
Huffman Coding

An efficient method of lossless data compression. Symbols appearing more
frequently are encoded with shorter bit strings while less frequent symbols
receive longer codes.

Reference: https://en.wikipedia.org/wiki/Huffman_coding

Complexity:
    Time:  O(n log n) for encoding (heap operations)
    Space: O(n) for the code table
"""

from __future__ import annotations

import heapq
from collections import defaultdict, deque


class Node:
    """A node in the Huffman tree."""

    def __init__(
        self,
        frequency: int = 0,
        sign: int | None = None,
        left: Node | None = None,
        right: Node | None = None,
    ) -> None:
        self.frequency = frequency
        self.sign = sign
        self.left = left
        self.right = right

    def __lt__(self, other: Node) -> bool:
        return self.frequency < other.frequency

    def __gt__(self, other: Node) -> bool:
        return self.frequency > other.frequency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return self.frequency == other.frequency

    def __str__(self) -> str:
        return "<ch: {0}: {1}>".format(self.sign, self.frequency)

    def __repr__(self) -> str:
        return "<ch: {0}: {1}>".format(self.sign, self.frequency)


class HuffmanReader:
    """Reads Huffman-encoded binary data from a file."""

    def __init__(self, file: object) -> None:
        self.file = file
        self.buffer: list[str] = []
        self.is_last_byte: bool = False

    def get_number_of_additional_bits_in_the_last_byte(self) -> int:
        """Read the 3-bit header indicating extra padding bits.

        Returns:
            The number of additional padding bits in the last byte.
        """
        bin_num = self.get_bit() + self.get_bit() + self.get_bit()
        return int(bin_num, 2)

    def load_tree(self) -> Node:
        """Reconstruct the Huffman tree from the file header.

        Returns:
            The root node of the reconstructed tree.
        """
        node_stack: deque[Node] = deque()
        queue_leaves: deque[Node] = deque()
        root = Node()

        current_node = root
        is_end_of_tree = False
        while not is_end_of_tree:
            current_bit = self.get_bit()
            if current_bit == "0":
                current_node.left = Node()
                current_node.right = Node()
                node_stack.append(current_node.right)
                current_node = current_node.left
            else:
                queue_leaves.append(current_node)
                if node_stack:
                    current_node = node_stack.pop()
                else:
                    is_end_of_tree = True

        self._fill_tree(queue_leaves)
        return root

    def _fill_tree(self, leaves_queue: deque[Node]) -> None:
        """Load character values into leaf nodes.

        Args:
            leaves_queue: Queue of leaf nodes to populate.
        """
        leaves_queue.reverse()
        while leaves_queue:
            node = leaves_queue.pop()
            char_value = int(self.get_byte(), 2)
            node.sign = char_value

    def _load_byte(self, buff_limit: int = 8) -> bool:
        """Load the next byte into the buffer if needed.

        Args:
            buff_limit: Minimum buffer size before loading.

        Returns:
            True if enough bits are available for reading.
        """
        if len(self.buffer) <= buff_limit:
            byte = self.file.read(1)
            if not byte:
                return False
            integer = int.from_bytes(byte, "big")
            self.buffer.extend(list("{0:08b}".format(integer)))
        return True

    def get_bit(self, buff_limit: int = 8) -> str | int:
        """Read a single bit from the buffer.

        Args:
            buff_limit: Minimum buffer size before loading.

        Returns:
            A '0' or '1' character, or -1 if at end of file.
        """
        if self._load_byte(buff_limit):
            return self.buffer.pop(0)
        return -1

    def get_byte(self) -> str | int:
        """Read eight bits from the buffer.

        Returns:
            An 8-character binary string, or -1 if at end of file.
        """
        if self._load_byte():
            byte_list = self.buffer[:8]
            self.buffer = self.buffer[8:]
            return "".join(byte_list)
        return -1


class HuffmanWriter:
    """Writes Huffman-encoded binary data to a file."""

    def __init__(self, file: object) -> None:
        self.file = file
        self.buffer: str = ""
        self.saved_bits: int = 0

    def write_char(self, char: str) -> None:
        """Write a character as its 8-bit ordinal value.

        Args:
            char: A single character to write.
        """
        self.write_int(ord(char))

    def write_int(self, num: int) -> None:
        """Write an integer as an 8-bit binary value.

        Args:
            num: An integer (0-255) to write.
        """
        bin_int = "{0:08b}".format(num)
        self.write_bits(bin_int)

    def write_bits(self, bits: str) -> None:
        """Write a string of bits, flushing complete bytes.

        Args:
            bits: A string of '0' and '1' characters.
        """
        self.saved_bits += len(bits)
        self.buffer += bits
        while len(self.buffer) >= 8:
            integer = int(self.buffer[:8], 2)
            self.file.write(bytes([integer]))
            self.buffer = self.buffer[8:]

    def save_tree(self, tree: Node) -> None:
        """Serialize the Huffman tree structure to the file.

        Args:
            tree: The root node of the Huffman tree.
        """
        signs: list[int] = []
        tree_code = ""

        def _get_code_tree(node: Node) -> None:
            nonlocal tree_code
            if node.sign is not None:
                signs.append(node.sign)
            if node.left:
                tree_code += "0"
                _get_code_tree(node.left)
            if node.right:
                tree_code += "1"
                _get_code_tree(node.right)

        _get_code_tree(tree)
        self.write_bits(tree_code + "1")
        for int_sign in signs:
            self.write_int(int_sign)

    def _save_information_about_additional_bits(
        self, additional_bits: int
    ) -> None:
        """Overwrite the first three bits to record padding count.

        Args:
            additional_bits: The number of padding bits appended.
        """
        self.file.seek(0)
        first_byte_raw = self.file.read(1)
        self.file.seek(0)
        first_byte = "{0:08b}".format(int.from_bytes(first_byte_raw, "big"))
        first_byte = "{0:03b}".format(additional_bits) + first_byte[3:]
        self.write_bits(first_byte)

    def close(self) -> None:
        """Flush remaining bits with padding and finalize the file."""
        additional_bits = 8 - len(self.buffer)
        if additional_bits != 8:
            self.write_bits("0" * additional_bits)
            self._save_information_about_additional_bits(additional_bits)


class TreeFinder:
    """Traverses a Huffman tree to decode individual symbols."""

    def __init__(self, tree: Node) -> None:
        self.root = tree
        self.current_node = tree
        self.found: int | str | None = None

    def find(self, bit: str) -> bool:
        """Advance one step in the tree and check for a decoded symbol.

        Args:
            bit: '0' for left, '1' for right.

        Returns:
            True if a symbol was found at the current node.
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
        return False

    def _reset(self, found: int | str = "") -> None:
        """Reset traversal to the root after finding a symbol.

        Args:
            found: The decoded symbol value.
        """
        self.found = found
        self.current_node = self.root


class HuffmanCoding:
    """Provides static methods for Huffman file encoding and decoding."""

    def __init__(self) -> None:
        pass

    @staticmethod
    def decode_file(file_in_name: str, file_out_name: str) -> None:
        """Decode a Huffman-encoded file.

        Args:
            file_in_name: Path to the encoded input file.
            file_out_name: Path to the decoded output file.
        """
        with open(file_in_name, "rb") as file_in, open(
            file_out_name, "wb"
        ) as file_out:
            reader = HuffmanReader(file_in)
            additional_bits = (
                reader.get_number_of_additional_bits_in_the_last_byte()
            )
            tree = reader.load_tree()
            HuffmanCoding._decode_and_write_signs_to_file(
                file_out, reader, tree, additional_bits
            )

    @staticmethod
    def _decode_and_write_signs_to_file(
        file: object,
        reader: HuffmanReader,
        tree: Node,
        additional_bits: int,
    ) -> None:
        """Decode bits from reader and write decoded bytes to file.

        Args:
            file: The output file object.
            reader: The HuffmanReader providing encoded bits.
            tree: The root of the Huffman tree.
            additional_bits: Number of padding bits in the last byte.
        """
        tree_finder = TreeFinder(tree)
        is_end_of_file = False

        while not is_end_of_file:
            bit = reader.get_bit()
            if bit != -1:
                while not tree_finder.find(bit):
                    bit = reader.get_bit(0)
                file.write(bytes([tree_finder.found]))
            else:
                is_end_of_file = True
                last_byte = reader.buffer
                last_byte = last_byte[:-additional_bits]
                for bit in last_byte:
                    if tree_finder.find(bit):
                        file.write(bytes([tree_finder.found]))

    @staticmethod
    def encode_file(file_in_name: str, file_out_name: str) -> None:
        """Encode a file using Huffman coding.

        Args:
            file_in_name: Path to the raw input file.
            file_out_name: Path to the encoded output file.
        """
        with open(file_in_name, "rb") as file_in, open(
            file_out_name, mode="wb+"
        ) as file_out:
            signs_frequency = HuffmanCoding._get_char_frequency(file_in)
            file_in.seek(0)
            tree = HuffmanCoding._create_tree(signs_frequency)
            codes = HuffmanCoding._generate_codes(tree)

            writer = HuffmanWriter(file_out)
            writer.write_bits("000")
            writer.save_tree(tree)
            HuffmanCoding._encode_and_write_signs_to_file(
                file_in, writer, codes
            )
            writer.close()

    @staticmethod
    def _encode_and_write_signs_to_file(
        file: object, writer: HuffmanWriter, codes: dict[int, str]
    ) -> None:
        """Read bytes from file and write their Huffman codes.

        Args:
            file: The input file object.
            writer: The HuffmanWriter for output.
            codes: Mapping of byte values to Huffman code strings.
        """
        sign = file.read(1)
        while sign:
            int_char = int.from_bytes(sign, "big")
            writer.write_bits(codes[int_char])
            sign = file.read(1)

    @staticmethod
    def _get_char_frequency(file: object) -> dict[int, int]:
        """Count byte frequencies in a file.

        Args:
            file: The input file object.

        Returns:
            A dict mapping byte values to their frequencies.
        """
        is_end_of_file = False
        signs_frequency: dict[int, int] = defaultdict(lambda: 0)
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
    def _generate_codes(tree: Node) -> dict[int, str]:
        """Generate Huffman codes from the tree.

        Args:
            tree: The root of the Huffman tree.

        Returns:
            A dict mapping byte values to their binary code strings.
        """
        codes: dict[int, str] = {}
        HuffmanCoding._go_through_tree_and_create_codes(tree, "", codes)
        return codes

    @staticmethod
    def _create_tree(signs_frequency: dict[int, int]) -> Node:
        """Build a Huffman tree from character frequencies.

        Args:
            signs_frequency: Mapping of byte values to frequencies.

        Returns:
            The root node of the constructed Huffman tree.
        """
        nodes = [
            Node(frequency=frequency, sign=char_int)
            for char_int, frequency in signs_frequency.items()
        ]
        heapq.heapify(nodes)

        while len(nodes) > 1:
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)
            new_node = Node(
                frequency=left.frequency + right.frequency,
                left=left,
                right=right,
            )
            heapq.heappush(nodes, new_node)

        return nodes[0]

    @staticmethod
    def _go_through_tree_and_create_codes(
        tree: Node, code: str, dict_codes: dict[int, str]
    ) -> None:
        """Recursively traverse the tree to build code mappings.

        Args:
            tree: The current node being visited.
            code: The accumulated bit string for this path.
            dict_codes: The output dict to populate.
        """
        if tree.sign is not None:
            dict_codes[tree.sign] = code

        if tree.left:
            HuffmanCoding._go_through_tree_and_create_codes(
                tree.left, code + "0", dict_codes
            )

        if tree.right:
            HuffmanCoding._go_through_tree_and_create_codes(
                tree.right, code + "1", dict_codes
            )
