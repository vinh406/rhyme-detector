# Import the g2p_en module
from g2p_en import G2p
g2p = G2p()

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

# Get the phonemes for a text
def get_phonemes(text, output_file):
    f = open(output_file, "w")
    for line in text:
        line = re.sub(r"[^a-zA-Z ]", "", line)
        for word in line.split(" "):
            # Seperate the syllables with hyphens
            syllables = syllabify(g2p(word))
            for syllable in syllables:
                for phoneme in syllable:
                    f.write(phoneme)
                if syllable != syllables[-1]:
                    f.write("-")
            if word != line.split(" ")[-1]:
                f.write(" ")
        f.write("\n")
    f.close()
