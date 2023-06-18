import random
import spacy

nlp = spacy.load('en_core_web_sm')

def construct_pangram_sentence(pangram):
    word_list = list(nlp.Defaults.stop_words)
    pangram_sentence = []
    for char in pangram:
        word = random.choice(word_list)
        pangram_sentence.append(word)
    pangram_sentence = " ".join(pangram_sentence).strip().capitalize() + "."
    return pangram_sentence
