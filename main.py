from phonemes import tokenize
from rhymes import check_rhyme
from jinja2 import Environment, FileSystemLoader

# Get the phonemes for a text
f = open("test/test.txt", "r")
text = f.readlines()
lines = tokenize(text)

# Group syllables into rhyming groups
group = 0
for i in range(len(lines)):
    for token in lines[i]:
        # If word is at the end of a line, check the end of next 3 lines
        if token == lines[i][-1]:
            for j in range(i + 1, min(i + 4, len(lines))):
                token2 = lines[j][-1]
                # Check each syllable
                for syllable in token.syllables:
                    for syllable2 in token2.syllables:
                        if check_rhyme(syllable.phonemes, syllable2.phonemes):
                            # Check if the syllable is already in a group
                            if syllable.group == 0 and syllable2.group == 0:
                                group += 1
                                syllable.group = group
                                syllable2.group = group
                            elif syllable.group == 0:
                                syllable.group = syllable2.group
                            elif syllable2.group == 0:
                                syllable2.group = syllable.group
        # Check words from one line against the next line
        for j in range(i, min(i + 2, len(lines))):
            for token2 in lines[j]:
                if token == token2:
                    continue
                # Check each syllable
                for syllable in token.syllables:
                    for syllable2 in token2.syllables:
                        if check_rhyme(syllable.phonemes, syllable2.phonemes):
                            # Check if the syllable is already in a group
                            if syllable.group == 0 and syllable2.group == 0:
                                group += 1
                                syllable.group = group
                                syllable2.group = group
                            elif syllable.group == 0:
                                syllable.group = syllable2.group
                            elif syllable2.group == 0:
                                syllable2.group = syllable.group

# Generate html
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("template.html")
output = template.render(lines=lines)
f = open("templates/ouput.html", "w")
f.write(output)
f.close()
