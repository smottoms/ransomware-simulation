from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
cipher = Fernet(key)

with open("key.key","wb") as f:
    f.write(key)

folder = "demo_files"

for file in os.listdir(folder):
    path = os.path.join(folder,file)

    if os.path.isfile(path):

        with open(path,"rb") as f:
            data = f.read()

        encrypted = cipher.encrypt(data)

        with open(path,"wb") as f:
            f.write(encrypted)

print("Files encrypted (Simulation)")