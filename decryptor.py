from cryptography.fernet import Fernet
import os

with open("key.key","rb") as f:
    key = f.read()

cipher = Fernet(key)

folder = "demo_files"

for file in os.listdir(folder):
    path = os.path.join(folder,file)

    with open(path,"rb") as f:
        data = f.read()

    decrypted = cipher.decrypt(data)

    with open(path,"wb") as f:
        f.write(decrypted)

print("Files restored successfully.")