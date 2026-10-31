tag_prob = {
    "the": {"DET": 0.9, "NOUN": 0.1},
    "dog": {"NOUN": 0.9, "VERB": 0.1},
    "runs": {"VERB": 0.8, "NOUN": 0.2},
    "cat": {"NOUN": 0.9, "VERB": 0.1}
}

text = input("Enter a sentence: ").lower().split()

for word in text:
    if word in tag_prob:
        tag = max(tag_prob[word], key=tag_prob[word].get)
    else:
        tag = "UNKNOWN"

    print(word, "->", tag)
