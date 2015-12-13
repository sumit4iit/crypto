from Crypto.Cipher import AES
obj = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
f = open('1-7.txt', 'r')
cip = ''
for line in f:
        cip += line

        print obj.decrypt(cip.decode('base64'))
