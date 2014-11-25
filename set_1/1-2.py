import sys
import binascii
""" Print XOR of two strings.
    usage: 1-2.py <str1> <str2>"""
str1 = sys.argv[1]
str2 = sys.argv[2]

xord = ''.join(chr(ord(c1) ^ ord(c2)) for c1,c2 in zip(binascii.unhexlify(str1), binascii.unhexlify(str2)))

print binascii.hexlify(xord)
