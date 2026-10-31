import re

text = "The boy is playing happily"
words = text.split()

for word in words:
    if re.match(r'^[Tt]he$', word):
        tag = "DET"
    elif re.match(r'.*ing$', word):
        tag = "VERB"
    elif re.match(r'.*ly$', word):
        tag = "ADV"
    elif word.lower() in ["is", "are", "was", "were"]:
        tag = "VERB"
    else:
        tag = "NOUN"

    print(word, "->", tag)
