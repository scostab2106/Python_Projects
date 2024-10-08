import pyautogui
import time

pyautogui.press('win')
pyautogui.write('paint')
time.sleep(2)
pyautogui.press('enter')

time.sleep(3)
pyautogui.click(x=234, y=284)

distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5)   # move down
    pyautogui.drag(-distance, 0, duration=0.5)  # move left
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.5)  # move up