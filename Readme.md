\# Steganography GUI Project

\## Overview

This project is a Steganography tool with a GUI that allows users to
securely hide secret messages inside image files and retrieve them using
a password. It supports encryption and decryption using a simple
user-friendly interface.

\### Real-World Applications

\- Secure communication to prevent unauthorized access - Digital
watermarking for copyright protection - Hidden data transmission in
sensitive environments

\## Features

\- Encrypt messages inside images (.png, .jpg, .jpeg, .bmp) -
Password-protected encryption and decryption - Automatic file naming to
prevent overwriting - User-friendly GUI for easy interaction - Windows
executable (.exe) support (planned for future enhancement)

\## Technologies Used

This project utilizes the following technologies:

\- \*\*Python\*\*: The core programming language used for encryption,
decryption, and GUI development. - \*\*OpenCV (cv2)\*\*: Used for image
processing, loading, modifying, and saving images with hidden
messages. - \*\*Tkinter\*\*: A built-in Python library used to create
the graphical user interface (GUI) for user interaction. -
\*\*NumPy\*\*: A powerful numerical computing library used for handling
pixel data efficiently. - \*\*Pillow (PIL)\*\*: Used for handling image
formats, ensuring compatibility, and making image manipulation easier.

\## Installation

\### 1️⃣ Clone the Repository

\`\`\`sh git clone https://github.com/AJAY25855/StegoVault.git \`\`\`

\### 2️⃣ Navigate to the Project Directory

\`\`\`sh cd StegoVault \`\`\`

\### 3️⃣ Install Dependencies

\`\`\`sh pip install -r requirements.txt \`\`\`

\## Usage

\### Running the GUI

\`\`\`sh python gui.py \`\`\`

\### Steps:

1\. Click \*\*Encryption\*\* → Enter your \*\*secret message\*\* and
\*\*password\*\* → Select an \*\*image\*\*. 2. Click \*\*Decryption\*\*
→ Enter the \*\*password\*\* to reveal the hidden message.

\## How It Works

\- \*\*Encryption\*\* modifies pixel values to embed the message
securely. - \*\*Decryption\*\* extracts the message \*\*only\*\* with
the correct password.

\### System Requirements

\- \*\*Operating System\*\*: Windows, Linux, macOS - \*\*Python
Version\*\*: 3.7 or later - \*\*Required Libraries\*\*: OpenCV, NumPy,
Pillow, Tkinter

\## Screenshots

\### GUI Main Screen

\### Encryption Window

\### Decryption Window

\## Future Enhancements

\- Support for more image formats - Enhanced encryption techniques -
Mobile app version - Windows executable (.exe) for easy execution
without requiring Python installation - Cloud-based steganography for
online data hiding

\## Contributing

If you\'d like to contribute, feel free to fork the repository and
submit a pull request!

\## License

This project is open-source and available under the MIT License.

\## Author

\- Kada Sai Datta Siva Naga Ajay Kumar
