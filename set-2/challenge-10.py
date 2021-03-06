import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.util import decode_base64, decrypt_ecb_with_cbc

# Given constants
key = b'YELLOW SUBMARINE'
iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Given input file
filename = "files/input-10.txt"

# Open file and read ciphertext
with open(filename) as file:
    ciphertext = decode_base64(file.read().replace("\n", ""))

# Decrypt ciphertext using ECB in CBC mode using given key
print(decrypt_ecb_with_cbc(ciphertext, key, iv))