def _get_chunks(cipher_txt, key_size):
    i = 0;
    tokens = []
    while i < len(cipher_txt):
        tokens.append(cipher_txt[i:i+key_size])
        i+=key_size
    
    return tokens

def _detect_ecb(chunks):
    while len(chunks):
        key = chunks[0]
        chunks = chunks[1:]
        if key in chunks:
            return True;
    return False;

def detect_aes_ecb(cipher_txt, key_size):
    return  _detect_ecb(_get_chunks(cipher_txt, key_size))
    
if __name__ == '__main__':
    f = open('1-8.txt', 'rb')
    for line in f:
        if detect_aes_ecb(line, 32):
            print line
