import operator
import pprint
# Break repeated key XOR cipher

def hammingDistance(str1, str2):
    """
    Calculate Hammind Distance between the two strings.
    Assumption is that both the string have the same length.
    """
    dist = 0
    for entry in [bin(ord(c1) ^ ord(c2))[2:] for c1,c2 in zip(str1, str2)]:
        dist += entry.count('1')
    return dist

def get_chunks(raw, size):
    i = 1
    chunks = []
    while size*i < len(raw):
        chunks.append(raw[size*(i-1):size*i])
    return chunks

def guessKeySize(rng, text, depth):
    keySizeProb = {}
    for keySize in range(1,rng):
        dist = 0.
        for i in range(depth):
            dist += hammingDistance(text[i*keySize:(i+1)*keySize], text[(i+1)*keySize:(i+2)*keySize])
        dist = dist/depth
        dist = dist/keySize
        keySizeProb[keySize] = dist
    lst = sorted(keySizeProb.items(), key=operator.itemgetter(1), reverse = False)
    return lst

if __name__ == '__main__':
    file = '6.txt'
    f = open(file,'r')
    txt = ''
    for line in f:
        txt += line.decode('base64')
    lst = guessKeySize(40, txt, 10)
    for entry in lst:
        print entry

## Tests
assert hammingDistance("this is a test", "wokka wokka!!!") == 37

