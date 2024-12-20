import os
import cryptography
from cryptography.fernet import Fernet
import cryptography.fernet

os.chdir("C:\\Users\\thekk\\Downloads\\New folder")
files = []
for file in os.listdir():
    if file == "thepass.key":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

with open("thepass.key", "rb") as thepass:
    secret_key = thepass.read()

for file in files:
    with open(file, "rb") as thefile:
        content = thefile.read()
    try:
        decrypted_contents = Fernet(secret_key).decrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(decrypted_contents)
        print(f"decrypted {file}")
    except cryptography.fernet.InvalidToken:
        print(f"cant decrypt {file}")
