import pytest
import pyautogui
import subprocess
import time

import random
import string
from datetime import datetime
import os

from locators import MainMenuPageLocators as MMPL

def generate_custom_string():
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{random_part}_{timestamp}"


def check_image_on_screen(expected_image_path):
    try:
        res = pyautogui.locateOnScreen(expected_image_path, confidence=0.85)
        return True
    except pyautogui.ImageNotFoundException:
        folder_path = os.path.dirname(expected_image_path)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(folder_path, f"fail_{timestamp}.png")
        
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        return False

@pytest.fixture(scope="function")
def lakioo():
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.5

    app_path = r"C:\Users\Sehii\AppData\Local\Programs\infokiosk\LAKIOO Creator.exe"  

    process = subprocess.Popen(
        app_path,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=False,
        creationflags=subprocess.CREATE_NO_WINDOW  # Отключает консольное окно (только для консольных .exe)
    )
    time.sleep(3)  

    yield process

    process.terminate() 
    process.wait() 


def test_create_new_project(lakioo):
    
    pyautogui.click(*MMPL.NEW_PROJECT)
    project_name = generate_custom_string()
    pyautogui.write(project_name)
    
    pyautogui.click(*MMPL.LITE_LICENSE_LEVEL)
    
    pyautogui.click(*MMPL.ACCEPT_BTN)
    
    res = check_image_on_screen('test_create_new_project/expected_res.png')
    assert res, "Získaný výsledok nezodpovedá očakávanému výsledku"
    
    
def test_open_exist_project(lakioo):
    
    pyautogui.click(*MMPL.MY_PROJECTS)
    
    pyautogui.doubleClick(*MMPL.FIRST_PROJECT)
    
    res = check_image_on_screen('test_open_exist_project/expected_res.png')
    assert res, "Získaný výsledok nezodpovedá očakávanému výsledku"
    
    
def test_open_exist_project_xfail(lakioo):
    
    pyautogui.click(*MMPL.MY_PROJECTS)
    
    pyautogui.click(*MMPL.FIRST_PROJECT)
    
    res = check_image_on_screen('test_open_exist_project_xfail/expected_res.png')
    assert res, "Získaný výsledok nezodpovedá očakávanému výsledku"
    
    