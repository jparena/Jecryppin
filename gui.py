import tkinter as tk
from tkinter import filedialog
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import os

def encrypt_folder():
    folder_path = filedialog.askdirectory(title="Select Folder to Jecryppt")
    if folder_path:
        key = key_entry.get().encode()
        key = key.ljust(32, b'\0')
        try:
            encrypt_folder_contents(folder_path, key)
            result_label.config(text="Folder has been Jecryppted successfully.")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")
    else:
        result_label.config(text="Error: No folder has been selected.")
def encrypt_file(file_path, key):
    # read the file content
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    # make an aes cipher object
    cipher = AES.new(key, AES.MODE_GCM)

    # encrypt the file
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # write the encrypted content back to the file
    with open(file_path, 'wb') as file:
        file.write(cipher.nonce)
        file.write(tag)
        file.write(ciphertext)
          
def encrypt_folder_contents(folder_path, key):
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			encrypt_file(file_path,key)
def decrypt_file():
    # gotta get file pathway
    file_path = filedialog.askopenfilename(title="Select File to Decrypt")
    if file_path:
        # needs user to impute key
        key = key_entry.get().encode()
        # pad key (256 bits)
        key = key.ljust(32, b'\0')
        print("Decryption Key:", key)

        # read encrypted file content
        with open(file_path, 'rb') as file:
            nonce = file.read(16)
            tag = file.read(16)
            ciphertext = file.read()

        print("Nonce:", nonce)
        print("Tag:", tag)
        print("Ciphertext:", ciphertext)

        # create aes cipher object
        try:
            cipher = AES.new(key, AES.MODE_GCM, nonce)

            # decrypt file content
            plaintext = cipher.decrypt_and_verify(ciphertext, tag)

            # put decrypted back into file
            with open(file_path, 'wb') as file:
                file.write(plaintext)
            result_label.config(text="I think I did it maybe..")
        except ValueError as e:
            print("Decryption Error:", str(e))
            result_label.config(text="Mmmmm, thats not right, sorry.")
    else:
        result_label.config(text="Error: No file has been selected.")
#Tkinter Starts
root = tk.Tk()
root.title("Jecryppin")
root.geometry("500x350")
root.configure(bg="white")

frame = tk.Frame(root, bg="white")
frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

key_label = tk.Label(frame, text="Please Enter Encryption/Decryption Key:",fg="#003EFF", bg="white")
key_label.pack()
key_entry = tk.Entry(frame, show ="*")
key_entry.pack()
#encrypt button
encrypt_button = tk.Button(frame, text="Encrypt Folder", command=encrypt_folder)
encrypt_button.pack(pady=10)

#  decrypt button
decrypt_button = tk.Button(frame, text="Decrypt File", command=decrypt_file)
decrypt_button.pack()

#  result
result_label = tk.Label(frame, text="", bg="white")
result_label.pack(pady=10)

#warning lol
warning_label = tk.Label(root, text="Warning:There is no forgot password option.", bg="white", fg="red")
warning_label.pack(side=tk.BOTTOM, pady=10)
root.mainloop()
