sentence = "Hello, are you a Human?"
words = sentence.split()
word_counts = {}

for words in words:
    if w in words:
        w = w.lower()
        if w in word_counts:
            word_counts[w] = word_counts[w] + 1
        else:
            word_counts[w] = 1
        
print(word_counts)