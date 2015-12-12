import sys

def h2a(hexStr):
    base64Str = hexStr.decode('hex').encode('base64')
    print base64Str

#if __name__ == __main__:
#    h2a(sys.argv[1])

h2a("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
