from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("SECRET NOTE")
window.minsize(width=400, height=400)

# Section where the user selects the title
title_label = Label(text="Enter Your Title", font=('Arial', 10, 'bold'), pady=10)
title_label.pack()

title_entry = Entry(width=20)
title_entry.pack()

# Section where the user enters the text to be encrypted
secret_label = Label(text="Enter Your Secret", font=('Arial', 10, 'bold'), pady=10)
secret_label.pack()

secret_entry = Entry(width=20)
secret_entry.pack()

# Section where the user enters the encryption key
master_label = Label(text="Enter Master Key", font=('Arial', 10, 'bold'), pady=10)
master_label.pack()

master_entry = Entry(width=20)
master_entry.pack()

folder_name = title_entry.get()

def caesar_encrypt(text, shift_amount):
    encrypted_text = ""
    try:
        for char in text:
            if char.isalpha():
                if char.isupper():
                    encrypted_char = chr(((ord(char) - ord('A') + int(shift_amount)) % 26) + ord('A'))
                else:
                    encrypted_char = chr(((ord(char) - ord('a') + int(shift_amount)) % 26) + ord('a'))
            else:
                encrypted_char = char

            encrypted_text += encrypted_char

        return encrypted_text
    except:
        messagebox.showerror("WARNING", "Invalid character")

def save_button_clicked():
    text = secret_entry.get()
    title = title_entry.get()
    shift_amount = master_entry.get()

    encrypted_text = caesar_encrypt(text, shift_amount)

    try:
        with open("secret.txt", 'a', encoding='utf-8') as my_file:
            my_file.write(f"\n{title}")
            my_file.write(f"\n{encrypted_text}")

    except:
        pass

def decrypter(text, shift_amount):
    decrypted_text = ""
    try:
        for char in text:
            if char.isalpha():
                if char.isupper():
                    decrypted_char = chr(((ord(char) - ord('A') - int(shift_amount)) % 26) + ord('A'))
                else:
                    decrypted_char = chr(((ord(char) - ord('a') - int(shift_amount)) % 26) + ord('a'))
            else:
                decrypted_char = char

            decrypted_text += decrypted_char

        return decrypted_text
    except:
        messagebox.showerror("WARNING", "Invalid character")

def decrypt_button_clicked():
    text = secret_entry.get()
    title = title_entry.get()
    shift_amount = master_entry.get()

    decrypted_text = decrypter(text, shift_amount)

    try:
        messagebox.showinfo(title="Decrypted Text", message=decrypted_text)

    except:
        pass

decrypt_button = Button(text="Save and Encrypt", command=save_button_clicked)
decrypt_button.pack()

decrypt_button = Button(text="Decrypt", command=decrypt_button_clicked)
decrypt_button.pack()

save_button_clicked()
window.mainloop()
