# Jecryppin

Jecryppin is a Python-based file encryption and decryption tool with a graphical user interface (GUI). It allows users to securely encrypt and decrypt files using the Advanced Encryption Standard (AES) algorithm.

## Features

- Encrypt files with a user-provided encryption key
- Decrypt files with the corresponding decryption key
- Graphical user interface (GUI) built with Tkinter
- Secure encryption using the AES algorithm
- Error handling for incorrect decryption keys

## Prerequisites

- Python 3.x
- Tkinter library
- pycryptodome library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/jecryppin.git
   ```

2. Install the required dependencies:
   ```
   pip install pycryptodome
   ```

## Usage

1. Run the `gui.py` file:
   ```
   python gui.py
   ```

2. The Jecryppin GUI window will appear.

3. To encrypt a file:
   - Click the "Encrypt File" button.
   - Select the file you want to encrypt using the file dialog.
   - Enter the encryption key in the provided input field.
   - Click the "Encrypt" button.
   - The encrypted file will be saved with the same name and location as the original file.

4. To decrypt a file:
   - Click the "Decrypt File" button.
   - Select the encrypted file you want to decrypt using the file dialog.
   - Enter the decryption key in the provided input field.
   - Click the "Decrypt" button.
   - If the decryption key is correct, the file will be decrypted and saved with the same name and location as the encrypted file.
   - If the decryption key is incorrect, an error message will be displayed.

## Warning

- Keep your encryption and decryption keys secure and do not share them with anyone.
- There is no "forgot password" option. If you lose your decryption key, you will not be able to decrypt your files.

## Contributing

If you find any issues or have suggestions for improvement, please tell.
