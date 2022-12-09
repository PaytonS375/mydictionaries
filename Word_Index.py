# EC - Dictionaries Exercise:
# Analyze the text of the book of John from the Bible and display how many times
# each of these words show up in the text - 'Father', 'God', 'Christ', 'Spirit', 'life', 'man' (case sensitive).
# (note: all punctuation marks, chapter and verse references have been removed to allow to analyze each word)

infile = open('book of John text.txt','r')

words = {}
words['words2'] = [" Father "," God ", " Christ ", " Spirit "," spirit "," life "," man "]

for w in infile:

    for t in w.split():
        t = " " + t + " "
        words[t] = w.count(t)

for word in words:

    if word in words['words2']:
        print(word + ':', words[word])