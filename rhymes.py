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

similar_vowels = [
    ['AA', 'AO', 'AH'],
    ['IY', 'IH'],
    ['UW', 'UH'],
    ['EH', 'AE'],
    ['EY', 'AY'],
    ['OW', 'AW'],
]

similar_consonants = [
    ['P', 'B'],
    ['T', 'D', ''],
    ['K', 'G'],
    ['F', 'V'],
    ['TH', 'DH'],
    ['S', 'Z', ''],
    ['SH', 'ZH'],
    ['CH', 'JH'],
    ['M', 'N'],
    ['L', 'R'],
    ['W', 'Y'],
    ['HH'],
]

def calculate_similarity_score(syllable1, syllable2):
    # Check empty syllables
    if syllable1 == [''] or syllable2 == ['']:
        return 0

    # Get the vowel and consonant sounds for each syllable
    consonants1 = []
    for phoneme in syllable1:
        if phoneme in arpa_vowels:
            v1 = phoneme
        else:
            consonants1.append(phoneme)

    consonants2 = []
    for phoneme in syllable2:
        if phoneme in arpa_vowels:
            v2 = phoneme
        else:
            consonants2.append(phoneme)
    
    # Compare vowel sounds
    if v1 == v2:
        vowel_score = 1
    elif any(v1 in group and v2 in group for group in similar_vowels):
        vowel_score = 0.75
    else:
        vowel_score = 0.5
    
    # Compare consonant sounds
    consonant_score = 1
    if len(consonants1) < len(consonants2):
        consonants1 += [''] * (len(consonants2) - len(consonants1))
    elif len(consonants2) < len(consonants1):
        consonants2 += [''] * (len(consonants1) - len(consonants2))        
    for i in range(len(consonants1)):
        if consonants1[i] == consonants2[i]:
            consonant_score *= 1
        elif any(consonants1[i] in group and consonants2[i] in group for group in similar_consonants):
            consonant_score *= 0.75
        else:
            consonant_score *= 0.5
    # Calculate overall similarity score
    total_score = vowel_score * 0.6 + consonant_score * 0.4

    return total_score

def remove_onset(syllable):
    for i in range(len(syllable)):
        if syllable[i] in arpa_vowels:
            return syllable[i:]
    return syllable

def check_rhyme(syllable1, syllable2):
    return calculate_similarity_score(remove_onset(syllable1), remove_onset(syllable2)) > 0.8