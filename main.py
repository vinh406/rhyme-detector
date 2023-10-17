from phonemes import get_phonemes

# Test the phoneme generator
f = open("test/test.txt", "r")
text = f.readlines()
get_phonemes(text, "test/phonemes.txt")