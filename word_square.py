from collections import Counter, deque

# Open and read the file containing valid words, storing the words in a set called '_words'.
with open('valid_words.txt', 'r') as dictionary_of_valid_words:
    _words = set(line.strip() for line in dictionary_of_valid_words)


class Trie:
    """A basic Trie (prefix tree) data structure."""

    def __init__(self):
        self.store = {}

    def add(self, word):
        """
        Add a word to the Trie. Adds a branch to the Trie data structure
        which ultimately corresponds to the word being added.

        Args:
        word (str): Word to be added to the Trie.
        """
        node = self.store
        for char in word:
            if char not in node:
                node[char] = {}  # If char is not in node, create a new dict for it.
            node = node[char]  # Go to the next level. The value of node[char] is dictionary.

    def _find_recurse(self, node, word: list):
        words = []
        if not node:
            return [''.join(word)]  # If the node is an empty dictionary {} it indicates the end of branch
            # If not True = False

        for key in node:
            word.append(key)
            words.extend(self._find_recurse(node[key], word))  # Adds an iterable i.e list to end of another list.
            word.pop()

        return words

    def find(self, prefix=''):
        node = self.store
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return self._find_recurse(node, list(prefix))


def possible(word, size, letter_count):
    # If the output of Counter(word) - letter_count is Counter then it is True
    if len(word) != size or Counter(word) - letter_count:
        return False
    return True


def _solve_for_column_and_row(size, trie, letters_remaining, square=None):
    square = square or deque()  # You can also read this as 'square = deque() if square is None else square'

    if len(square) == size:
        return square

    if not square:
        prefix = ''
    else:
        prefix_chars = []
        # Iterate over the words in the square
        for word in square:
            char = word[len(square)]
            prefix_chars.append(char)
        prefix = ''.join(prefix_chars)
    possible_words = trie.find(prefix)

    for word in possible_words:
        letters_in_word = Counter(word)
        if letters_in_word - letters_remaining:
            continue

        square.append(word)
        square = _solve_for_column_and_row(size, trie, letters_remaining - letters_in_word, square)

        if len(square) == size:
            return square

        square.pop()

    return square


def wordsquare(size, letters):
    """
    Creates a word square of a specific 'size (int)' using the 'letters (str)' provided.

    Args:
    size (int): The size of the word square (i.e., the length of each word which also reflects the number
    of rows and columns.).
    letters (str): The letters to use to create the words.

    Returns:
    str: The completed word square, if one is found.
    """

    letter_count = Counter(letters)

    possible_words = set()
    for word in _words:
        if possible(word, size, letter_count):
            possible_words.add(word)

    trie = Trie()  # Initialize an empty Trie data structure.
    for word in possible_words:
        trie.add(word)

    result = _solve_for_column_and_row(size, trie, letter_count)
    if not result:
        return 'No word square could be found for that input'
    # Checks if the letters used in the final word square are exactly the same as the original letters provided.
    assert (sorted(''.join(result)) == sorted(letters))
    return '\n'.join(result)


def test():
    test_inputs = '''\
4 aaccdeeeemmnnnoo
5 aaaeeeefhhmoonssrrrrttttw
5 aabbeeeeeeeehmosrrrruttvv
7 aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy'''

    for case in test_inputs.splitlines():
        size, letters = case.strip().split()
        size = int(size)
        result = wordsquare(size, letters)
        print(f'\n{result}\n')


if __name__ == '__main__':
    test()
