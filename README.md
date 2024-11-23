# Stega Shade CLI 📷

[![Help Screen](https://media.discordapp.net/attachments/1289621011263914106/1309985024149295194/image.png?ex=67439220&is=674240a0&hm=0809af596f8e5fcc38232f50d58a9a32b7914779c3fd486253261baf51935354&=&format=webp&quality=lossless)](help.png)

<p align="right"> <img src="https://komarev.com/ghpvc/?username=merwin-asm-april4&label=Project%20views&color=0e75b6&style=flat" /> </p>

## Overview

Stega Shade CLI is a user-friendly command-line interface tool designed for image-based steganography. With a focus on simplicity and security, it provides functionality to encode and decode messages into images, including password-protected encoding for enhanced privacy. The tool is built using Python and leverages robust algorithms to ensure data integrity and secrecy.

---

## Features

- **Simple Steganography**:
  Encode and decode messages into images without requiring additional security layers. Perfect for casual use cases.
  
- **Protected Steganography**:
  Password-protected encoding ensures only authorized users can decode the hidden message. Uses **AES encryption** for robust security.

- **User-Friendly Interface**:
  Intuitive CLI with a visually appealing help guide powered by the `rich` library.

- **Error Handling**:
  Graceful handling of incorrect inputs and error scenarios with helpful feedback.

---

## Installation
```bash
pip install stegashade
```

## Commands and Usage

### Help Command
Displays all available commands and their descriptions.

```bash
stegashade help
```
---

## Commands and Usage

### Encode Simple
Embed a simple message into an image.

```bash
stegashade encode_simple <image_path> <output_path> <data>
```

Example

```bash
stegashade encode_simple input.png output.png "Hello, world!"
```

### Decode Simple
Extract a message embedded using simple steganography.

```bash
stegashade decode_simple <image_path>
```

Example
```bash
stegashade decode_simple output.png
```

### Encode Protected
Embed a password-protected message into an image.

```bash
stegashade encode_protected <image_path> <output_path> <data> <password>
```

Example
```bash
stegashade encode_protected input.png output.png "Secret Data" "my_secure_password"
```

### Decode Protected
Extract a password-protected message from an image.

```bash
stegashade decode_protected <image_path> <password>
```

Example
```bash
stegashade decode_protected output.png "my_secure_password"
```

---

## How It Works

### Simple Steganography
1. The algorithm encodes the binary representation of a message into the least significant bits (LSBs) of pixel values in the image.
2. Minor changes in the LSBs are imperceptible to the human eye, keeping the message hidden without noticeably altering the image.

### Protected Steganography
1. The message is encrypted using **AES encryption** before embedding it into the image.
2. AES (Advanced Encryption Standard) ensures that the embedded data is highly secure and accessible only with the correct password.
3. The encrypted data is then processed similarly to the simple steganography method, embedding it into the image’s pixel values.

---

## Allowed Characters for Messages

Due to the limitations of the algorithm, only a specific set of characters can be used in messages:

- **Letters**: A-Z, a-z
- **Numbers**: 0-9
- **Punctuation Marks**: `! @ # $ % ^ & * ( ) _ + - = [ ] { } | ; : ' , . < > / ? ~`
- **Whitespace**: Spaces

**Note**: Non-ASCII characters, emojis, or extended Unicode are not supported.

---

## Advantages of Stega Shade

1. **Data Security**: 
   - Protected steganography leverages **AES encryption**, requiring a password for decoding. This ensures that only authorized users can access the hidden data.

2. **Image Integrity**: 
   - The algorithm makes minimal changes to the pixel values, maintaining the image quality while embedding the message.

3. **Versatility**: 
   - Supports both simple steganography (for casual use) and protected steganography (for secure communications).

4. **Efficiency**: 
   - Processes images efficiently, even for large file sizes, making it suitable for practical applications.

5. **Rich CLI Interface**: 
   - Provides a visually appealing command-line experience with clear instructions and error feedback, thanks to the `rich` Python library.

---

## Why Is It Unique?

- **Dual Modes**: Offers both simple and AES-encrypted steganography, catering to users with varying security needs.
- **AES Encryption**: Ensures strong encryption, adding an advanced layer of security to embedded messages.
- **User Experience**: The CLI tool is intuitive, visually engaging, and user-friendly, making it accessible to both beginners and experts.
- **Minimal Impact**: Maintains the original image’s visual fidelity while effectively hiding the message.

---

