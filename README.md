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

# 📋 Test Scenario Example: test_create_new_project

## Test Name

Verification of New Project Creation with Lite License

## Objective

To verify that the project creation functionality in the application works correctly. The test ensures a new project is created with a unique name and a Lite license, and that the expected result is displayed on the screen.

## Prerequisites

- The `lakioo` fixture is provided to the test. It handles the automatic opening and closing of the application.
- **Manual launch of the application is NOT required.** If the application is already open before the test starts, it may cause a duplicate window, which could result in test failure.
- The `pyautogui` library is properly configured and able to control UI interactions.
- The `expected_res.png` file exists in the `test_create_new_project/` directory and contains the expected visual result.
- Constants `MMPL.NEW_PROJECT`, `MMPL.LITE_LICENSE_LEVEL`, and `MMPL.ACCEPT_BTN` are defined and contain valid screen coordinates.
- The `generate_custom_string()` function is available and returns a unique string.
- The `check_image_on_screen()` function is implemented and capable of accurately comparing the current screen with the reference image.

## Test Steps

1. **Click on the New Project button**

   - Use `pyautogui.click(*MMPL.NEW_PROJECT)` to open the project creation form.

2. **Enter Project Name**

   - Generate a unique name using `generate_custom_string()`.
   - Input the name using `pyautogui.write(project_name)`.

3. **Select Lite License Level**

   - Click at the coordinates `MMPL.LITE_LICENSE_LEVEL` to choose the Lite license.

4. **Confirm Project Creation**

   - Click `MMPL.ACCEPT_BTN` to confirm and proceed with the project creation.

5. **Verify Result**

   - Use `check_image_on_screen('test_create_new_project/expected_res.png')` to compare the screen with the reference image.
   - Store the result in `res`.

## Expected Result

- The `res` variable should be `True`, indicating a successful project creation.
- If `res` is `False`, the test fails with the message:
  > "Získaný výsledok nezodpovedá očakávanému výsledku"

## Postconditions

- A project with the generated name and Lite license is created in the application.
- The UI displays the correct result matching `expected_res.png`.

## Notes

- Test stability depends on the accuracy of coordinate values in the `MMPL` constants.
- UI layout changes or screen resolution/scaling issues may cause test failures.
- It is advised to validate the `check_image_on_screen()` function under multiple environments.

## Test Type

Positive, automated UI test

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
