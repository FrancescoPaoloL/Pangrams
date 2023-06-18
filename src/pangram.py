import string
from random_pangram import generate_random_pangram
from sentence_constructor import construct_pangram_sentence

def generate_pangram(alphabet=None):
    if alphabet is None:
        # Use the default alphabet if not provided
        alphabet = list(string.ascii_lowercase)

    # Generate a pangram
    pangram = generate_random_pangram(alphabet)

    # Create a sentence with meaningful words
    pangram_sentence = construct_pangram_sentence(pangram)

    return pangram_sentence
