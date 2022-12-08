# EC - Dictionaries Exercise:
# Analyze the text of the book of John from the Bible and display how many times
# each of these words show up in the text - 'Father', 'God', 'Christ', 'Spirit', 'life', 'man' (case sensitive).
# (note: all punctuation marks, chapter and verse references have been removed to allow to analyze each word)

import csv

infile = open('book of John text.txt','r')

words = {}

for w in infile:

    for t in w.split():
        words[t] = w.count(t)

for word in words:
    print('Father: ' + str(words[word]))
    print('God: ' + str(words[word]))
    print('Christ: ' + str(words[word]))
    print('Spirit: ' + str(words[word]))
    print('life: ' + str(words[word]))
    print('man: ' + str(words[word]))