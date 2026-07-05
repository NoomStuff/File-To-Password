# 🔐 File to Password

Generate a secure password using any file and a password key.

```
Enter file name: Example.png
Enter a password key: test
Confirm password key: test


Generated Password: fUux)J4Hz9&R3CG7iiLk
Press enter to copy and close...
```

---

## 🔍 How to Use

1. Make sure you have everything required to run the script (see below).
2. Run the script.
3. Enter the name and extension of a file in the same folder as the script (eg. `Example.png`).
4. Enter a password key (eg. `MyPassword123`). Your input will be hidden when typing.
5. Verify the password by entering it again, or skip this step by pressing enter.
6. You will now see the generated password unless you run the script with `-H` or `--hidden`. Press enter to copy it to your clipboard and close the program.

## 🔧 Requirements to Run

- Python 3.6+
- `cryptography` package (`pip install -r requirements.txt`)

---

### ⚙️ How It Works:

This Python script generates a strong password using a file and a password key. The output of the program can not be decrypted and will always be the same if the input is the same, any small change will give a completely different result. The generated password should always pass the requirements for any site.

1. **File Selection**: When running the program, you will be prompted to enter the name of a file. The file must be in the same folder as the script, and you need to include the name and extension of the file (eg. `Example.png`). Any file type should work.
2. **Password Key**: After selecting a valid file, you will be prompted to enter a password key. You can enter any text here (eg. `MyPassword123`). It is important that you remember the key, as it will be used to generate the password.

3. **Password Confirmation**: You will be asked to confirm your password key. You can re-enter it or just press enter to skip the confirmation step. It is recommended to retype the password when creating it for the first time.

4. **Password Generation**: Your file is hashed using SHA-256, and part of that file hash is used as the salt for PBKDF2. Your password key is then passed through PBKDF2-HMAC-SHA256 to produce deterministic bytes. Those bytes are mapped directly to allowed password characters, ensuring the final password is valid anywhere. The characters are then shuffled deterministically, so the same file and password key always produce the same 20-character password.

5. **Copying the Password**: Once the password is generated, you can either manually copy it or press enter to automatically copy it to your clipboard and close the script. If you start the program with `-H` or `--hidden`, the displayed password will be masked while the real password is still copied to the clipboard.

6. **Reusing the Password**: The output password you get from the program will always be the same if your file data and password key are _EXACTLY_ the same, any change to the file content (name excluded) or the key will give you a completely different password.

---

You are free to use the project however you want, I don't care. Credit would be appreciated if you use it for something tho.
