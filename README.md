<h1 align="center">MaMi 🤖📱</h1>h1>

**MaMi** is your **multipurpose ADB toolkit** to manage, extract, uninstall, and explore Android apps **straight from your terminal**.

> Fast, simple and hacker-friendly.  
> _Built by a pentester, for pentesters._

---

## ✨ **Key features**

✅ List all **user-installed apps** with clean numbering  
✅ Download `/data/data/<package>` folders easily  
✅ Uninstall user apps in seconds  
✅ Interactive CLI — easy navigation and clear menus  
✅ Auto-clears your terminal for a clean workflow  
✅ Handles `Ctrl + C` gracefully to exit without mess

---

## 🚀 **Coming soon**

- 📦 Install APKs directly from the terminal  
- 🔍 Search specific app info and permissions  
- 🗄️ Full app data backups  
- 🗒️ Logging & auditing  
- 🔐 PIN/pattern brute forcing *(optional)*

---

## ⚙️ **Requirements**

- Python 3.7+  
- `adb` installed and working (`adb devices`)  
- Root permissions on the device (needed for `/data/data` access)

---

## ⚡ **Installation**

```bash
git clone https://github.com/yourusername/mami.git
cd mami
# Make sure adb is in your PATH
python3 mami.py
```

---

## 🧑‍💻 Quick usage
```bash
python3 mami.py
```

Basic flow: 

1️⃣ List user-installed apps   
2️⃣ Pick an app by number  
3️⃣ Download app data folder or uninstall the app   
4️⃣ Return to main menu or exit anytime with Ctrl + C

---

## 📂 Project structure
```bash
mami/
 ├── mami.py     # Main script
 ├── README.md   # This file
 └── ...         # (future modules)
```

---

💚 Contributing
PRs, feature ideas and feedback are always welcome!
Open an issue or ping me directly.

---


👨‍💻 Author
Made by [p314d0](https://www.linkedin.com/in/nicolasgula/)  
MaMi — Your Android hacking friend.

---

📜 License
MIT License — use, fork, share freely.

---















