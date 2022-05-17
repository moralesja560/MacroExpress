#This script enables the PC to open SCADA successfully.
######
import pyautogui
import time
import os
import sys
pyautogui.FAILSAFE = True


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

pyautogui.hotkey('win','r')
pyautogui.write('msedge.exe 10.65.64.27/startupcs.html')
pyautogui.press('enter')
time.sleep(10)
#pyautogui.hotkey('winleft','up')
time.sleep(10)
#pyautogui.press('f4')
#pyautogui.write('10.65.64.27/startupcs.html')
#pyautogui.press('enter')
pyautogui.click(1801,55)
time.sleep(10)
pyautogui.write('pantalla mtto')
pyautogui.press('tab')
pyautogui.write('mttopant')
pyautogui.press('enter')
time.sleep(10)
#locate Vision General button
scada_btn = pyautogui.locateOnScreen(resource_path(r"images/scadabutton.jpg"),grayscale=True, confidence=.7)
#center the button
button7point = pyautogui.center(scada_btn)
#divide button coordinates into x and y3
button7x, button7y = button7point
pyautogui.click(button7x, button7y)
sys.exit()
