# VigenereCipher

## Overview
VigenereCipher is a Python-based application that provides a user-friendly interface for encrypting and decrypting messages using the Vigenère cipher. The application is built using the Tkinter library for the graphical user interface (GUI).

## Features
- **Encrypt Messages**: Encrypt any message using a provided key or a randomly generated key.
- **Decrypt Messages**: Decrypt any encrypted message using the provided key.
- **Random Key Generation**: Automatically generate a random key if none is provided during encryption.
- **Copy to Clipboard**: Easily copy the encrypted or decrypted message to the clipboard with a single click.
- **User-Friendly Interface**: A simple and intuitive GUI to perform encryption and decryption operations.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/ghosthasgone/VigenereCipher.git
    ```
2. Navigate to the project directory:
    ```sh
    cd VigenereCipher
    ```
3. Make sure you have python installed:

## Usage
1. Run the application:
    ```sh
    py main.py
    ```
2. The application window will open, presenting options to encrypt or decrypt a message.

### Encrypting a Message
1. Select the "Encrypt" option.
2. Enter the message you want to encrypt in the "Message" field.
3. Enter a key in the "Key" field (optional). If no key is provided, a random key will be generated.
4. Click the "Execute" button.
5. The encrypted message and the key used will be displayed.

### Decrypting a Message
1. Select the "Decrypt" option.
2. Enter the encrypted message in the "Message" field.
3. Enter the key used for encryption in the "Key" field.
4. Click the "Execute" button.
5. The decrypted message will be displayed.

### Copying to Clipboard
- Click on the displayed message to copy it to the clipboard. A confirmation message will appear.

## Code Explanation

### Key Generation
The `generate_key` function generates a random key of a specified length using ASCII letters.

### Encryption
The `vigenere_encrypt` function encrypts a message using the Vigenère cipher algorithm. It shifts each character in the message by the corresponding character in the key.

### Decryption
The `vigenere_decrypt` function decrypts an encrypted message using the Vigenère cipher algorithm. It reverses the shift applied during encryption.

### GUI Components
- **Main Window**: The main application window is created using Tkinter.
- **Action Frame**: Contains radio buttons to select between encryption and decryption.
- **Message Entry**: Input field for the message to be encrypted or decrypted.
- **Key Entry**: Input field for the key used in encryption or decryption.
- **Result Label**: Displays the encrypted or decrypted message.
- **Execute Button**: Executes the encryption or decryption based on the selected action.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements
- The Tkinter library for providing the GUI components.
- The Python community for their continuous support and contributions.
