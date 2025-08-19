Here you go — the complete **README.md** in Markdown format that you can directly copy and paste:

```markdown
# 🕵️‍♂️ Invisible QR  

Invisible QR is a fun and creative project that combines **QR Code generation** with **steganography**.  
It hides a secret message inside a QR code image using **Least Significant Bit (LSB)** encoding, making the QR code appear normal but secretly carrying hidden information.  

---

## ✨ Features  
- ✅ Generate a standard QR code.  
- ✅ Hide secret messages inside the QR code image using **LSB steganography**.  
- ✅ Extract hidden messages from the invisible QR code.  
- ✅ Simple and lightweight (uses `qrcode`, `Pillow`, and `stegano`).  

---

## 📂 Project Structure  

```

invisible-qr/
│── invisibleqr.py      # Generate invisible QR with hidden data
│── decodeqr.py         # Extract hidden data from invisible QR
│── qr\_code.png         # Normal QR code (auto-generated)
│── invisible\_qr.png    # Invisible QR with secret hidden inside
│── README.md           # Project documentation

````

---

## ⚙️ Installation  

Make sure you have **Python 3.7+** installed.  
Install the dependencies:  

```bash
pip install qrcode[pil] pillow stegano
````

---

## 🚀 Usage

### 1️⃣ Generate Invisible QR

Run the following command to create an invisible QR code with a hidden message:

```bash
python invisibleqr.py
```

* This will generate:

  * `qr_code.png` → Normal QR code.
  * `invisible_qr.png` → Invisible QR with hidden message embedded.

---

### 2️⃣ Decode Invisible QR

Run the following command to reveal the hidden message:

```bash
python decodeqr.py
```

Example output:

```
✅ Hidden message found: If you reading this, then you are interested in knowing what can I do....
```

---

## 🔍 How It Works

1. **QR Code Generation**

   * A normal QR code is created using the `qrcode` library.

2. **Steganography (Hiding Data)**

   * The secret message is embedded inside the QR image using **LSB (Least Significant Bit)** steganography via the `stegano` library.

3. **Extraction (Decoding)**

   * The hidden message is retrieved by scanning the LSB bits of the image.

---

## 📸 Example

* **Normal QR (`qr_code.png`)**
  ![QR Code](qr_code.png)

* **Invisible QR (`invisible_qr.png`)**
  *(Looks the same, but secretly contains hidden text!)*

---

## 🛡️ Disclaimer

This project is created **for educational purposes only**.
Do **not** use it for malicious activities such as hiding sensitive data illegally.

---

## 👨‍💻 Author

Developed by **\[Jay Dosi (Sacred-Beast)]** ✨


