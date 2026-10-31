import random
from nltk import bigrams, word_tokenize
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

text = "I like NLP. I like Python. I enjoy NLP."
words = word_tokenize(text.lower())

pairs = list(bigrams(words))
model = {}

for w1, w2 in pairs:
    model.setdefault(w1, []).append(w2)

word = "i"
sentence = [word]

for _ in range(8):
    if word not in model:
        break
    word = random.choice(model[word])
    sentence.append(word)

print("Generated Text:", " ".join(sentence))
