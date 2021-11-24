# # PIP INSTALL PYAUTOGUI
# # ALAN WALKER LOGO
#
import pyautogui
import time
time.sleep(2)
pyautogui.hotkey('ctrl', 'esc')
time.sleep(1)
pyautogui.write("paint", interval = 0.1)
time.sleep(1)
pyautogui.press("enter")


time.sleep(5)

pyautogui.dragRel(250, -500, duration = 0.25)
pyautogui.dragRel(250, 575, duration = 0.25)
pyautogui.moveRel(0, -650, duration = 0.25)
pyautogui.moveRel(-575, 0, duration = 0.25)
pyautogui.dragRel(200, 650, duration = 0.25)
pyautogui.dragRel(110, -250, duration = 0.25)
pyautogui.dragRel(110, 250, duration = 0.25)
pyautogui.dragRel(200, -600, duration = 0.25)
