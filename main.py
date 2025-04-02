import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_key(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def vigenere_encrypt(message, key):
    encrypted_message = []
    key_length = len(key)
    for i, char in enumerate(message):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            if char.islower():
                encrypted_message.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                encrypted_message.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            encrypted_message.append(char)
    return ''.join(encrypted_message)

def vigenere_decrypt(encrypted_message, key):
    decrypted_message = []
    key_length = len(key)
    for i, char in enumerate(encrypted_message):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            if char.islower():
                decrypted_message.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            else:
                decrypted_message.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        else:
            decrypted_message.append(char)
    return ''.join(decrypted_message)

def encrypt_message():
    message = message_entry.get()
    key = key_entry.get()
    if not key:
        key = generate_key(len(message))
        key_entry.insert(0, key)
    encrypted_message = vigenere_encrypt(message, key)
    result_text.set(f"Message: {encrypted_message}\n\n Key: {key}")

def decrypt_message():
    key = key_entry.get()
    if not key:
        messagebox.showerror("Error", "Key cannot be empty for decryption")
        return
    encrypted_message = message_entry.get()
    decrypted_message = vigenere_decrypt(encrypted_message, key)
    result_text.set(f"Message: {decrypted_message}")

def update_ui():
    message_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    result_text.set("")

def center_window(window):
    window.update_idletasks()
    width = 500
    height = 300
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def copy_to_clipboard(event):
    app.clipboard_clear()
    app.clipboard_append(result_text.get())
    messagebox.showinfo("Copied", "Text copied to clipboard")

app = tk.Tk()
app.title("Vigenère Cipher")

# Center the window
center_window(app)

# Styling
app.configure(bg='#282e34')
for widget in app.winfo_children():
    widget.configure(bg='#282e34', fg='#ffffff')

action_frame = tk.Frame(app, bg='#282e34')
action_frame.pack(pady=10)

action_label = tk.Label(action_frame, text="Choose action:", bg='#282e34', fg='#ffffff')
action_label.pack(side=tk.LEFT)

action_var = tk.StringVar(value="encrypt")
encrypt_radio = tk.Radiobutton(action_frame, text="Encrypt", variable=action_var, value="encrypt", bg='#282e34', fg='#ffffff', command=update_ui, indicatoron=0, width=10, selectcolor='#4F4F4F')
encrypt_radio.pack(side=tk.LEFT)
decrypt_radio = tk.Radiobutton(action_frame, text="Decrypt", variable=action_var, value="decrypt", bg='#282e34', fg='#ffffff', command=update_ui, indicatoron=0, width=10, selectcolor='#4F4F4F')
decrypt_radio.pack(side=tk.LEFT)

message_label = tk.Label(app, text="Message:", bg='#282e34', fg='#ffffff')
message_label.pack()
message_entry = tk.Entry(app, width=50)
message_entry.pack()

key_label = tk.Label(app, text="Key:", bg='#282e34', fg='#ffffff')
key_label.pack()
key_entry = tk.Entry(app, width=50)
key_entry.pack()

result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, wraplength=400, bg='#282e34', fg='#ffffff')
result_label.pack(pady=10)
result_label.bind("<Button-1>", copy_to_clipboard)

action_button = tk.Button(app, text="Execute", command=lambda: encrypt_message() if action_var.get() == "encrypt" else decrypt_message(), bg='#4F4F4F', fg='#ffffff')
action_button.pack(pady=10)

app.mainloop()