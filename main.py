from phonemes import get_phonemes, get_unstressed
from rhymes import check_rhyme, remove_onset

# Test the phoneme generator
f = open("test/test.txt", "r")
text = f.readlines()
get_phonemes(text, "test/phonemes.txt")