import random

def generate_random_pangram(alphabet):
    pangram = ""
    while len(set(pangram)) != 26:
        random.shuffle(alphabet)
        pangram = "".join(alphabet)
    return pangram
