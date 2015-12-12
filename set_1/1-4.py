#Single byte XOR
import operator
import pprint

def bruteKeys(data):
    """
    Brute force all single byte keys on the data and return a list of deciphered strings
    """
    decStrs = []
    for key in range(0xff):
        dec = ''
        for x in range(2, len(data), 2):
            token = int(data[x-2:x], 16)
            #We need to map 0xa to 0x0a for this logic to work
            dec += hex(token^key)[2:].zfill(2)
        decStrs.append(dec.decode('hex'))
    return decStrs


def bestGuess(strings):
    """
    rank strings according to similarity to english language
    """
    lst = {}
    keywords=['the', 'be', 'to', 'a', 'of', 'and', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us']
    for string in strings:
        count = 0
        for k in keywords:
            if k in string:
                count+=1
        
        if count > 0:
            lst[string] = count
#    lst = sorted(lst.items(), key=operator.itemgetter(1), reverse = True)
    return lst

if __name__ == '__main__':
    f = open('1-4.txt', 'r')
    totDict = {}
    for line in f:
        totDict = dict(totDict, **bestGuess(bruteKeys(line)))
    
    lst = sorted(totDict.items(), key=operator.itemgetter(1), reverse = True)
    for entry in lst:
        print entry

