import sys

"""
Implementing repeating key XOR encryption
"""

f = open('1-5.txt')
key = sys.argv[1]

j = 0
for s in f:
    res = ''
    for i in range(len(s)):
        res += hex(ord(s[i]) ^ ord(key[j%len(key)]))[2:]
        j+=1

    print res
