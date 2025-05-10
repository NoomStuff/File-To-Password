import os
import hashlib
import base64
import string
import getpass
import time
import subprocess

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

valid_characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+?."

def hash_file(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    file_hash = hashlib.sha256(file_data).digest()
    return file_hash

def filter_safe_chars(text):
    return ''.join(c for c in text if c in valid_characters)

def generate_password(file_hash, password_key, length=20):
    file_salt = file_hash[:16]
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=file_salt,
        iterations=100000,
        backend=default_backend()
    )

    key = kdf.derive(password_key.encode())
    
    generated_password = base64.b85encode(key).decode()
    generated_password_filtered = filter_safe_chars(generated_password)
    return generated_password_filtered[:length]


def get_file():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    while True:
        file = input("Enter file name: ")
        path = os.path.join(script_dir, file)
        if os.path.isfile(path):
            return path
        else:
            print(f"'{path}' does not exist. Try again.\n")

def get_password():
    while True:
        password = getpass.getpass("[Input Hidden] Enter a password key: ")
        password_confirm = getpass.getpass("[Input Hidden] Confirm password key: ")
        
        if password == password_confirm:
            return password
        elif password_confirm == "":
            print("Confirmation skipped")
            return password
        else:
            print("Passwords don't match. Try again.\n")

file_path = get_file()
password_key = get_password()

hashed_file = hash_file(file_path)
generated_password = generate_password(hashed_file, password_key)

print(f"\n\nGenerated Password: {generated_password}")

input("Press enter to copy and close...")
try:
    subprocess.run("clip", text=True, input=generated_password)
    print("\nPassword copied!")
except Exception as e:
    print("\nCould not copy to clipboard.")
time.sleep(0.5)
