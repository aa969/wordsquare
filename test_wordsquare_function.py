import unittest
from collections import Counter

from word_square import Trie, possible


class TestWordSquare(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()
        self.words = ['ball', 'area', 'lady']
        for word in self.words:
            self.trie.add(word)

    def test_trie_find(self):
        self.assertEqual(self.trie.find('b'), ['ball'])
        self.assertEqual(self.trie.find('ba'), ['ball'])
        self.assertEqual(self.trie.find('bal'), ['ball'])
        self.assertEqual(self.trie.find('are'), ['area'])
        self.assertEqual(self.trie.find('lad'), ['lady'])
        self.assertEqual(self.trie.find(''), self.words)

    def test_possible(self):
        letters = Counter('ball')
        self.assertTrue(possible('ball', 4, letters))
        self.assertFalse(possible('area', 4, letters))
        self.assertFalse(possible('balll', 4, letters))
        self.assertFalse(possible('bat', 4, letters))
