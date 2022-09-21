import csv

infile = open('info_security.txt','r')

outfile = open('encrypted.txt','w')

codes = {'A': '!',
'B': '@',
'C': '#',
'D': '$',
'E': '%',
'F': '^',
'G': '&',
'H': '*',
'I': '(',
'J': ')',
'K': '+',
'L': '=',
'M': '`',
'N': '>',
'O': '<',
'P': '?',
'Q': ';',
'R': ':',
'S': '/',
'T': ',',
'U': '.',
'V': '1',
'W': '2',
'X': '3',
'Y': '4',
'Z': '5',
'a': '6',
'b': '7',
'c': '8',
'd': '9',
'e': 'q',
'f': 'w',
'g': 'e',
'h': 'r',
'i': 't',
'j': 'y',
'k': 'u',
'l': 'i',
'm': 'o',
'n': 'p',
'o': 'a',
'p': 's',
'q': 'd',
'r': 'f',
's': 'g',
't': 'h',
'u': 'j',
'v': 'k',
'w': 'l',
'x': 'c',
'y': 'x',
'z': 'n',
' ': ' ',
'.': 'v',
':': 'm'
}

message = ''

for word in infile:
    
    for c in word:
        message += codes[c]

# print(message) <-- reference for notes

outfile.write(message)