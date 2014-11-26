import sys

def hamming_distance(s1, s2):
    """
    Expects that string s1 and s2 are passed as a hex string.
    [call ''.encode('hex') before passing it as an argument]
    Computing number of bits that two strings differ in should do the trick.
    """
    # Make strings of even size.
    # Should not have any other side effect.
    if len(s1)%2 != 0:
        s1 = s1+'0'
    if len(s2)%2 != 0:
        s2 = s2+'0'

    # Make strings of equal length.
    # For the sake of sanity.
    if len(s2)<len(s1):
        s2 = s2+(len(s1) - len(s2))*'0'
    if len(s2)<len(s1):
        s1 = s1+(len(s2) - len(s1))*'0'


    cnt = 0
    res = int(s1,16) ^ int(s2,16)

    while res!=0:
        if res%2==1:
            cnt+=1
        res=res>>1

    return cnt


def key_length(txt):
    # Single iteratino works for now.
    # TODO:// Add extra iterations and take avarage.
    dkt = {}
    for length in range(2,40):
        dkt[length] = (hamming_distance(txt[:length], txt[length:2*length]))/float(length)

    return dkt


def transpose_blocks(txt, keyLen):
    lst = []
    for i in range(keyLen):
        lst.append('')
    for i in len(txt):
        lst[i%keyLen] = txt[i]
    return lst


#Milestone 1. Make code agree to the hamming distance of 37.
print hamming_distance("this is a test".encode('hex'),"wokka wokka!!!".encode('hex'))

#Milestone 2. Guess the key length.
#Shouldn't be that difficult.
file = '6.txt'
f = open(file,'r')
txt = ''
for line in f:
    txt += line.decode('base64').encode('hex')

dkt = key_length(txt)

for k,v in dkt.items():
    print str(k) +"\t:\t"+ str(v)
