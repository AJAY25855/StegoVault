import cv2
import hashlib

def decrypt_message(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Error loading image. Make sure the file path is correct.")

    binary_message = ""
    height, width, _ = img.shape

    for i in range(height):
        for j in range(width):
            for k in range(3):
                binary_message += str(img[i, j, k] & 1)

    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if message.endswith("###"):
            break
        message += char

    # Extract stored password and hidden message
    try:
        stored_hash, hidden_message = message.split(":", 1)
    except ValueError:
        raise ValueError("Decryption failed. Incorrect encoding or modified image.")

    # Hash the entered password and compare
    entered_hash = hashlib.sha256(password.encode()).hexdigest()
    if entered_hash != stored_hash:
        raise ValueError("Incorrect password! Decryption failed.")

    return hidden_message[:-3]  # Removing delimiter
