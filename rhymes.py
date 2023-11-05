from Levenshtein import ratio
arpa_vowels = [
        "AA",
        "AE",
        "AH",
        "AO",
        "AW",
        "AY",
        "EH",
        "ER",
        "EY",
        "IH",
        "IY",
        "OW",
        "OY",
        "UH",
        "UW",
    ]

def remove_onset(syllable):
    for i in range(len(syllable)):
        if syllable[i] in arpa_vowels:
            return syllable[i:]
    return syllable

def check_rhyme(syllable1, syllable2):
    return ratio(remove_onset(syllable1), remove_onset(syllable2)) > 0.7