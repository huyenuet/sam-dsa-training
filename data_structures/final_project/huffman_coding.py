from data_structures.queue.double_ended_queue import Queue
import sys


class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None


def get_sorted_char_frequency_list(text):
    # count frequency of appearance of each character
    char_frequency_dict = {}
    for char in text:
        if char in char_frequency_dict:
            char_frequency_dict[char] += 1
        else:
            char_frequency_dict[char] = 1

    # sort the char - frequency dict by frequency
    char_frequency_sorted_ls = list()
    for key, value in char_frequency_dict.items():
        if not char_frequency_sorted_ls:
            char_frequency_sorted_ls.append((key, value))
            continue

        for index, item in enumerate(char_frequency_sorted_ls):
            if value < item[1]:
                char_frequency_sorted_ls.insert(index, (key, value))
                break
        else:
            char_frequency_sorted_ls.append((key, value))

    return char_frequency_sorted_ls


class Huffman:

    def __init__(self):
        pass

    def encoding(self, string):
        """
        :param string: a sentence needed to encode
        :return: encoded_data, tree
        """
        huffman_tree = self.build_huffman_tree(string)
        huffman_code = self._encode_recursion(huffman_tree, "", {})
        encoded_data = ""
        for char in string:
            encoded_data += huffman_code[char]
        return encoded_data, huffman_tree

    def _encode_recursion(self, node: TreeNode, code_string: str, huffman_code: dict):
        if node is None:
            return
        if not node.left and not node.right:
            huffman_code[node.key] = code_string

        self._encode_recursion(node.left, code_string + "0", huffman_code)
        self._encode_recursion(node.right, code_string + "1", huffman_code)

        return huffman_code

    def decoding(self, encoded_string, huffman_tree):
        """
        :param encoded_string: data has been encoded
        :param huffman_tree: huffman tree used to decode data
        :return: decoded data
        """
        decoded_string = ''
        index = -1
        while index < len(encoded_string) - 2:
            decoded_char, index = self._decode_recursion(huffman_tree, encoded_string, index)
            decoded_string += decoded_char
        return decoded_string

    def _decode_recursion(self, huffman_tree, encoded_string, index):
        decoded_char = ''
        if huffman_tree is None:
            return

        # found a leaf node
        if huffman_tree.left is None and huffman_tree.right is None:
            decoded_char += huffman_tree.key
            return decoded_char, index

        index += 1
        if encoded_string[index] == '0':
            decoded_char, index = self._decode_recursion(huffman_tree.left, encoded_string, index)
        else:
            decoded_char, index = self._decode_recursion(huffman_tree.right, encoded_string, index)

        return decoded_char, index

    def build_huffman_tree(self, text):

        sorted_char_freq_list = get_sorted_char_frequency_list(text)

        # define 2 queues
        q1 = Queue()
        q2 = Queue()

        # assign each (char, frequency) to a leaf node, then add to q1
        for char, freq in sorted_char_freq_list:
            leaf_node = TreeNode(key=char, value=freq)
            q1.enqueue(leaf_node)

        def _find_minimum(queue1: Queue, queue2: Queue):
            if queue2.is_empty():
                return queue1.dequeue()
            if queue1.is_empty():
                return queue2.dequeue()
            if queue1.top().value >= queue2.top().value:
                return queue2.dequeue()
            else:
                return queue1.dequeue()

        while not (q1.is_empty() and q2.size() == 1):
            # get 2 nodes had lowest frequency characters from 2 queues and put them under a new node
            # add this node to q2

            left = _find_minimum(q1, q2)
            right = _find_minimum(q1, q2)
            new_node = TreeNode('$', left.value + right.value)
            new_node.left = left
            new_node.right = right
            q2.enqueue(new_node)

        huffman_tree = q2.dequeue()
        self.trim_huffman_tree(huffman_tree)
        return huffman_tree

    def trim_huffman_tree(self, tree):
        """remove the frequencies from the previously built tree"""
        tree.value = None
        if tree.left:
            self.trim_huffman_tree(tree.left)
        if tree.right:
            self.trim_huffman_tree(tree.right)


def huffman_encoding(text):
    huffman = Huffman()
    return huffman.encoding(text)


def huffman_decoding(encoded_string, huffman_tree):
    huffman = Huffman()
    return huffman.decoding(encoded_string, huffman_tree)


if __name__ == "__main__":
    code = {}
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
