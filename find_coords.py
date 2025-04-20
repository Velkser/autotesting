import pyautogui
import time
import mouse  # pip install mouse


already_clicked = False

try:
    while True:
        if mouse.is_pressed(button='left'):
            if not already_clicked:  
                x, y = pyautogui.position()
                print(f"Clicked at ({x}, {y})")
                already_clicked = True
        else:
            already_clicked = False
        time.sleep(0.01)  
except KeyboardInterrupt:
    print("\nEnd.")
