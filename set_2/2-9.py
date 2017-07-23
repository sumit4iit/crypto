def pkcs7_pad(plain_text, key_size):
    bytes_to_add = (key_size - len(plain_text) % key_size) % key_size
    return (plain_text.encode('hex') + '{:02x}'.format(bytes_to_add)*bytes_to_add).decode('hex')


print pkcs7_pad("YELLOW SUBMARINE", 20)