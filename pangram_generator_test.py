import unittest
from sentence_constructor import construct_pangram_sentence
from pangram import generate_pangram


class PangramGeneratorTests(unittest.TestCase):
    def test_construct_pangram_sentence(self):
        pangram = 'abcdefghijklmnopqrstuvwxyz'
        sentence = construct_pangram_sentence(pangram)
        self.assertEqual(sentence[:1], sentence[:1].upper())
        self.assertEqual(sentence[-1:], '.')
        self.assertEqual(len(sentence.split()), len(pangram))
        self.assertNotIn('abcdefghijklmnopqrstuvwxyz', sentence)

    def test_generate_pangram(self):
        input_alphabet = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']
        pangram = generate_pangram(input_alphabet)
        self.assertTrue(pangram[0].isalpha())  # Check if the first character is a letter
        self.assertTrue(pangram.endswith('.'))
        self.assertNotIn('abcdefghijklmnopqrstuvwxyz', pangram)
        self.assertEqual(len(pangram.split()), len(input_alphabet))

    # def test_generate_pangram(self):
    #     pangram = generate_pangram()
    #     self.assertTrue(pangram[0].isalpha())  # Check if the first character is a letter
    #     self.assertTrue(pangram.endswith('.'))
    #     self.assertNotIn('abcdefghijklmnopqrstuvwxyz', pangram)
    #     self.assertEqual(len(pangram.split()), 26)

if __name__ == '__main__':
    unittest.main()
