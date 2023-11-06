# Import the g2p model
from dp.phonemizer import Phonemizer

phonemizer = Phonemizer.from_checkpoint("en_us_cmudict_forward.pt")

import re
from syllabifier import syllabifyARPA


# Hyphenate a word based on its phonemes
def syllabify(pronunciation):
    syllabified = []
    try:
        for syllable in syllabifyARPA(pronunciation):
            syllabified.append(syllable.split(" "))
    except ValueError:
        syllabified.append(pronunciation)
    return syllabified


# Get the unstressed pronounciation of a word
def get_unstressed(word):
    phonemes = phonemizer(word, lang="en_us")
    phonemes = re.sub(r"[,?!.()-]", "", phonemes)
    phonemes = phonemes.split("][")
    phonemes = [p.strip("[]") for p in phonemes]
    return phonemes


# Get the phonemes for a text
def get_phonemes(text):
    out = []
    for line in text:
        line_out = []
        for word in line.split(" "):
            # Seperate the syllables with hyphens
            syllables = syllabify(get_unstressed(word))
            line_out.append(syllables)
        out.append(line_out)
    return out


# Print the phonemes for a text to a file
def print_phonemes(text, output_file):
    f = open(output_file, "w")
    for line in text:
        f.write(line)
        for word in line.split(" "):
            # Seperate the syllables with hyphens
            syllables = syllabify(get_unstressed(word))
            for syllable in syllables:
                for phoneme in syllable:
                    f.write(phoneme)
                if syllable != syllables[-1]:
                    f.write("-")
            if word != line.split(" ")[-1]:
                f.write(" ")
        f.write("\n")
    f.close()


class Token:
    def __init__(self, word):
        self.word = word
        self.syllables = []

    class Syllable:
        def __init__(self, phonemes):
            self.phonemes = phonemes
            self.group = 0

    def add_syllables(self, syllables):
        for syllable in syllables:
            self.syllables.append(Token.Syllable(syllable))


def preprocess(text):
    res = []
    for line in text:
        line = re.sub(r"\([^)]*\)", "", line)
        res.append(line)
    return res


def tokenize(lines):
    preprocessed = preprocess(lines)
    tokens = []
    for line in preprocessed:
        token_line = []
        for word in line.split(" "):
            # Seperate the syllables with hyphens
            token_word = Token(word)
            token_word.add_syllables(syllabify(get_unstressed(word)))
            token_line.append(token_word)
        tokens.append(token_line)
    return tokens
