import os
import hashlib
import string
import getpass
import time
import subprocess
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-H", "--hidden", action="store_true", help="Hide final generated password.")
ARGS = parser.parse_args()

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def hash_file(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    file_hash = hashlib.sha256(file_data).digest()
    return file_hash

def generate_password(file_hash, password_key, length=20):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    uppercase_characters = string.ascii_uppercase
    lowercase_characters = string.ascii_lowercase
    number_characters = string.digits
    special_characters = "!@#$%^&*()?"

    valid_characters = uppercase_characters + lowercase_characters + number_characters + special_characters
    file_salt = file_hash[:16]

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=64,
        salt=file_salt,
        iterations=100000,
        backend=default_backend()
    )

    key = kdf.derive(password_key.encode())

    required_characters = [
        uppercase_characters[key[0] % len(uppercase_characters)],
        lowercase_characters[key[1] % len(lowercase_characters)],
        number_characters[key[2] % len(number_characters)],
        special_characters[key[3] % len(special_characters)]
    ]

    remaining_characters = [
        valid_characters[key[i] % len(valid_characters)]
        for i in range(4, length)
    ]

    password_characters = required_characters + remaining_characters

    for i in range(len(password_characters) - 1, 0, -1):
        swap_index = key[i] % (i + 1)
        password_characters[i], password_characters[swap_index] = password_characters[swap_index], password_characters[i]

    return ''.join(password_characters)

def get_file():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    while True:
        file = input("Enter file name: ")
        
        paths = glob.glob(f"{script_dir}/{file}**", recursive=True)
        path = None
        
        if len(paths) > 1:
            print(f"'{file}' is ambiguous between the following paths:")
            for p in paths:
                print(f"  - {p}")
            print("Please specify the file name more clearly.\n")
            continue
        elif len(paths) == 1:
            path = paths[0]
        elif os.path.isfile(os.path.join(script_dir, file)):
            path = os.path.join(script_dir, file)
        
        if len(paths) == 0 or path is None or not os.path.isfile(path):
            print(f"'{file}' was not found. Try again.\n")
            continue
        
        return path

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
            
def mask_password(password):
    return '*' * len(password)

file_path = get_file()
password_key = get_password()

hashed_file = hash_file(file_path)
generated_password = generate_password(hashed_file, password_key)

if ARGS.hidden:
    print(f"\n\nGenerated Password: {mask_password(generated_password)}")
else:
    print(f"\n\nGenerated Password: {generated_password}")

input("Press enter to copy and close...")
try:
    subprocess.run("clip", text=True, input=generated_password)
    print("\nPassword copied!")
except Exception as e:
    print("\nCould not copy to clipboard.")
time.sleep(0.5)
