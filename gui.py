import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import cv2
import numpy as np
import os
import time

# Function to encrypt message
def encrypt_message():
    img_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All Files", "*.*")])
    if not img_path:
        return
    
    img = cv2.imread(img_path)
    if img is None:
        messagebox.showerror("Error", "Invalid image path!")
        return
    
    msg = simpledialog.askstring("Encryption", "Enter secret message:")
    password = simpledialog.askstring("Encryption", "Enter a password:", show='*')
    
    if not msg or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return
    
    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0
    
    # Store password in the first few pixels
    pass_encoded = password + "::" + msg + "::END"  # Store password followed by message with an end marker
    
    for char in pass_encoded:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    # Save with a unique name to prevent overwriting
    timestamp = int(time.time())
    encrypted_image = f"encrypted_{timestamp}.png"
    cv2.imwrite(encrypted_image, img)
    os.system(encrypted_image)
    messagebox.showinfo("Success", f"Message encrypted and saved as {encrypted_image}")

# Function to decrypt message
def decrypt_message():
    img_path = filedialog.askopenfilename(title="Select Encrypted Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All Files", "*.*")])
    if not img_path:
        return
    
    img = cv2.imread(img_path)
    if img is None:
        messagebox.showerror("Error", "Invalid image path!")
        return
    
    c = {i: chr(i) for i in range(255)}
    extracted_data = ""
    n, m, z = 0, 0, 0
    
    try:
        while True:
            char = c[img[n, m, z]]
            if extracted_data.endswith("::END"):
                extracted_data = extracted_data[:-5]  # Remove the END marker
                break
            extracted_data += char
            n += 1
            m += 1
            z = (z + 1) % 3
    except KeyError:
        pass  # Stop reading when an invalid pixel value is encountered
    
    # Extract password and message
    if "::" in extracted_data:
        stored_password, message = extracted_data.split("::", 1)
    else:
        messagebox.showerror("Error", "Invalid encrypted data!")
        return
    
    entered_password = simpledialog.askstring("Decryption", "Enter password:", show='*')
    
    if entered_password == stored_password:
        messagebox.showinfo("Decryption", f"Decrypted message: {message}")
    else:
        messagebox.showerror("Error", "Incorrect password!")

# GUI Setup
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("300x200")

tk.Label(root, text="Choose an option:", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Encryption", command=encrypt_message, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Decryption", command=decrypt_message, font=("Arial", 12)).pack(pady=5)

root.mainloop()
