import sys
import binascii
import operator
"""Sinlge byte XOR decrypt"""

lst = {}
#s = sys.argv[1]
keywords=['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us']

def isEnglish(a):
    cnt = 0
    for k in keywords:
        if a.find(k)!=-1:
            cnt+=1
    if cnt>0:
#        print a + " count: " + str(cnt)
        lst[a] = cnt

def decrypt(s):
    for i in range(255):
        s2 = ''
        for j in range(0,len(s),2):
            res = int(s[j]+s[j+1],16) ^ i
            s2+=str(hex(res)[2:])

        if len(s2)%2 == 0:
            isEnglish(s2.decode('hex'))


if __name__ == "__main__":
    f = open('test.txt')
    for line in f:
        if len(line)%2!=0:
            line = line[:-1]
        decrypt(str(line))
    f.close()
#    decrypt(sys.argv[1])
    sorted_lst = sorted(lst.items(), key=operator.itemgetter(1), reverse=True)
    for key,value in sorted_lst:
        print key
