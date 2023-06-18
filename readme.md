# Pangrams
A Pangram is essentially a sentence that uses all the letters of the alphabet.
According to <a href="https://en.wikipedia.org/wiki/Pangram" target="blank">Wikipedia</a> the best-known English pangram is <i>"The quick brown fox jumps over the lazy dog".</i>
This script makes a pangram every time it be executed.
The idea is simple:
- a pangram contains words which begins with all the letters of the alphabet;
- so we make a list with the all alphabet letters
- we shuffle them and
- we constrict a sentenceusing every letter in the alphabet list.

Ex.
Given: <br>
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

we make this: <br>
['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']

and, finally, we construct a sentence like <br>
<i>'brave cats dart effortlessly for good-hearted individuals juggling keenly like mindful nannies openly promoting quick reactions swiftly to unitedly visualize x-rayed zebras androgynously.'</i>

To do that we've used a Spacy NLP library that offers pre-trained language models for various languages; specifically,we've used 'en_core_web_sm' language model which provides various functionalities for processing and analyzing English text,including features like tokenization (that is splitting text into individual words or tokens), part-of-speech tagging, named entity recognition, syntactic parsing, and more.


which refers to the English language model with small size.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## Languages and Tools
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Requirements
```
spacy==3.3.0
```

## Test coverage
TODO

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>

## Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/francescopl/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="francescopaololezza" height="20" width="30" /></a>
<a href="https://www.kaggle.com/francescopaolol" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="francescopaololezza" height="20" width="30" /></a>
</p>



