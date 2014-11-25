#convert hex to base64
import binascii
import sys

def h2a(hexStr):
    base64Str = hexStr.decode('hex').encode('base64')
    print base64Str

if __name__ == "__main__":
if len(sys.argv) == 1:
    print "converts hex string to base64"
    print "usage : {0} <hex_string>".format(sys.argv[0])
else:
    h2a(sys.argv[1])
