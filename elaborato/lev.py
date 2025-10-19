import Levenshtein

def correct(word, dictionary, word_freq):
    candidates = sorted(dictionary, key=lambda w: (Levenshtein.distance(word, w), -word_freq.get(w, 0)))
    return candidates[0]

dictionary = ["casa", "cassa", "caso", "cane"]
word_freq = {"casa": 1000, "cassa": 100, "caso": 500, "cane": 700}

print(correct("cassa", dictionary, word_freq))  # Restituisce 'cassa'
print(correct("casae", dictionary, word_freq))  # Restituisce 'casa'
