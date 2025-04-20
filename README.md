# 🖱️ LAKIOO Creator UI Tests

Automated UI tests for the **LAKIOO Creator** Windows application, built with Python using PyAutoGUI and PyTest.

## 📦 Features

- 📁 Test for creating a new project  
- 📂 Test for opening an existing project  
- ❌ Failing test example (to simulate `xfail`)  
- 📸 Image matching on screen  
- 🧪 Screenshot capture on failure  
- 📍 Mouse click position tracker

---

## 🚀 Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Velkser/autotesting
cd autotesting
```

2. **(Optional) Create a virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## 🧪 Running the tests

```bash
pytest -v main.py
```

The tests will automatically launch `LAKIOO Creator.exe`, simulate user interactions, and compare the result with expected images.

---

## 📁 Project Structure

```
lakioo-ui-tests/
├── locators.py                      # Coordinates of UI elements
├── main.py                          # Main test suite and helper functions
├── mouse_locator.py                 # Tool to detect mouse click positions
├── requirements.txt                 # Dependencies
├── test_create_new_project/
│   └── expected_res.png             # Expected screenshot
├── test_open_exist_project/
│   └── expected_res.png
└── ...
```

---

## 🧠 Tech Stack

- `PyAutoGUI` — UI automation
- `PyTest` — testing framework
- `Pillow` — image processing
- `mouse` — detecting mouse clicks

---

## ⚠️ Notes

- Your screen resolution must remain constant.
- UI layout must match the reference images exactly.
- Make sure `LAKIOO Creator.exe` is installed at the defined path.

---

## 📸 Failure Screenshots

If the expected image is not found on screen, a screenshot will be automatically captured and saved in the same directory with a `fail_` prefix.

---

## 📍 Mouse Position Tool

To find screen coordinates of elements:

```bash
python mouse_locator.py
```

Click anywhere — positions will be printed to the console. Press Ctrl+C to stop.

---

## 👨‍💻 Author

**Sehii**  
Made with ❤️ using PyAutoGUI and Python.
