# 🔐 2FA Authenticator Web App

A lightweight web-based Two-Factor Authentication (2FA) app built using **Flask** and **JavaScript**. It allows users to add TOTP accounts via manual key input or QR code scanning, with live code generation and smooth UI animations.

> Built to function like Google Authenticator – right in your browser!

---

## ✨ Features

- 🔐 Generate **TOTP** codes (Time-based One-Time Passwords)
- 📷 **Scan QR codes** using webcam or image upload
- 💡 Toggle between **Light/Dark** mode (persists via `localStorage`)
- 🧹 Add, rename, and delete accounts with animations
- 🧠 Accounts stored in `accounts.json` for **persistence**
- ⏱️ Circular countdown timers for code refresh
- 🖱️ Built-in rename and delete buttons with hover effects

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **QR Scanning**: [html5-qrcode](https://github.com/mebjas/html5-qrcode)
- **Icons**: [Unicons](https://iconscout.com/unicons)
- **TOTP**: [pyotp](https://pyauth.github.io/pyotp/)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/deep-sengupta/2fa-authenticator.git
cd 2fa-authenticator
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip3 install flask pyotp
```

### 4. Run the App

```bash
python3 app.py
```

---

## 📂 Data Persistence
All added accounts and their secrets are stored in accounts.json. This ensures:
- Accounts persist even after restarting the server.
- No data is lost unless accounts.json is deleted.

---

## ⚠️ Security Note
- Never expose this app to the public internet without implementing proper authentication.
- Secrets are stored in plain JSON, so anyone with access to the file has access to your 2FA accounts.
- This project is intended for local use or educational purposes only.

---

## 🧪 Want to Extend?
Ideas:
- Add encrypted storage using cryptography
- Export/Import backup
- Login authentication to protect the UI
- PWA support to install as a mobile app
