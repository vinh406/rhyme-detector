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
    vowel1 = syllable1[0]
    vowel2 = syllable2[0]
    v1 = vowel1[:-1]
    v2 = vowel2[:-1]
    consonants1 = syllable1[1:]
    consonants2 = syllable2[1:]
    
    # Compare vowel sounds
    if vowel1 == 'AH0' and vowel2 == 'ER0' or vowel1 == 'ER0' and vowel2 == 'AH0':
        vowel_score = 0.85
    elif v1 == v2:
        vowel_score = 1
    elif any(v1 in group and v2 in group for group in similar_vowels):
        vowel_score = 0.75
    else:
        vowel_score = 0.5

    # Compare vowel stress
    if vowel1[-1] == vowel2[-1] or vowel1[-1] == '1' and vowel2[-1] == '2' or vowel1[-1] == '2' and vowel2[-1] == '1':
        vowel_score *= 1
    else:
        vowel_score *= 0.85

    # If there are no consonants, return the vowel score
    if len(consonants1) == 0 and len(consonants2) == 0:
        return vowel_score

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
        if ['A', 'E', 'I', 'O', 'U'].count(syllable[i][0]) > 0:
            return syllable[i:]
    return syllable

def check_rhyme(syllable1, syllable2):
    return calculate_similarity_score(remove_onset(syllable1), remove_onset(syllable2)) > 0.8
