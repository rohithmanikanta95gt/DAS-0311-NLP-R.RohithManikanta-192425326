text = "The boy is playing"
words = text.split()

tags = []

for word in words:
    if word.lower() in ["the", "a", "an"]:
        tags.append("DET")
    elif word.lower() in ["is", "are", "was", "were"]:
        tags.append("NOUN")
    else:
        tags.append("NOUN")

# Transformation rule: words following "is" are verbs if ending in "ing"
for i in range(1, len(words)):
    if words[i - 1].lower() == "is" and words[i].endswith("ing"):
        tags[i] = "VERB"

# Correct the tag of auxiliary verb "is"
for i, word in enumerate(words):
    if word.lower() == "is":
        tags[i] = "VERB"

for word, tag in zip(words, tags):
    print(word, "->", tag)
