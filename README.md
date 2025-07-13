# File to Password

Generate a secure password using a file and a key.  
Made by [NoomStuff](https://github.com/NoomStuff).  
Licensed under the MIT License. See [LICENSE](LICENSE).  
You are free to use the project however you want, but please provide credit when redistributing.

---

## How to Use

1. Make sure you have everything required to run the script (see below).
2. Run the script.
3. Enter the name and extension of a file in the same folder as the script (eg. `ExampleFile.png`).
4. Enter a password key (eg. `MyPassword123`). Your input will be hidden when typing.
5. Verify the password by entering it again, or skip this step by pressing enter.
6. You will now see the generated password. Press enter to copy it to your clipboard and close the program.

---

## Requirements to Run

- Python 3.6+
- `cryptography` package (`pip install cryptography`)

---

### How It Works:
This Python script generates a strong password using a file and a password key. The output of the program can not be decrypted and will always be the same if the input is the same, any small change will give a completely different result.

1. **File Selection**: When running the program, you will be prompted to enter the name of a file. The file must be in the same folder as the script, and you need to include the name and extension of the file (eg. `ExampleFile.png`). Any file type should work.
   
2. **Password Key**: After selecting a valid file, you will be prompted to enter a password key. You can enter any text here (eg. `MyPassword123`). It is important that you remember the key, as it will be used to generate the password.

3. **Password Confirmation**: You will be asked to confirm your password key. You can re-enter it or just press enter to skip the confirmation step. It is recommended to confirm the password when creating it for the first time.

4. **Password Generation**: Your file and password key are combined, hashed using SHA-256 (with the file hash as a salt), and encoded using PBKDF2. The resulting password is then base-85 encoded. A filter removes characters that might not be allowed in passwords, and the final password is truncated to 20 characters.

5. **Copying the Password**: Once the password is generated, you can either manually copy it or press enter to automatically copy it to your clipboard and close the program.

6. **Reusing the Password**: The output password you get from the program will always be the same if your file data and password key are *EXACTLY* the same, any change to the file (name excluded) or the key will give you a completely different password.

---

## License

This project is licensed under the MIT License.
> See the [LICENSE](LICENSE) file for full details.

---
