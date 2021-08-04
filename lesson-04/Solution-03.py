import random
import string

message = input("Enter message: ")
code = []

for length in range(len(message)):
    code.append(random.choice(string.ascii_letters))


def xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1, s2)])


encrypted = xor(message, code)
print(encrypted)

decrypted = xor(encrypted, code)
print(decrypted)
