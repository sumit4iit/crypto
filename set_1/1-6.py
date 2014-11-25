import sys

def hamming_distance(s1, s2):
    """
    Expects that string s1 and s2 are passed as a hex string.
    [call ''.encode('hex') before passing it as an argument]
    Computing number of bits that two strings differ in should do the trick.
    """

    cnt = 0
    res = int(s1,16) ^ int(s2,16)

    while res!=0:
        if res%2==1:
            cnt+=1
        res=res>>1

    return cnt



#Milestone 1. Make code agree to the hamming distance of 37.
print hamming_distance("this is a test".encode('hex'),"wokka wokka!!!".encode('hex'))

#Milestone 2.
