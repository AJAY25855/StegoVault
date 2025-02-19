import cv2
import hashlib

def encrypt_message(image_path, output_image, message, password):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Error loading image. Make sure the file path is correct.")
    
    # Hash the password for security
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    message = password_hash + ":" + message + "###"  # Adding password and delimiter
    message_bin = ''.join(format(ord(char), '08b') for char in message)

    height, width, _ = img.shape
    max_bits = height * width * 3

    if len(message_bin) > max_bits:
        raise ValueError("Message is too long to hide in the selected image!")

    idx = 0
    for i in range(height):
        for j in range(width):
            for k in range(3):
                if idx < len(message_bin):
                    img[i, j, k] = (img[i, j, k] & 254) | int(message_bin[idx])
                    idx += 1
                else:
                    break

    cv2.imwrite(output_image, img)
