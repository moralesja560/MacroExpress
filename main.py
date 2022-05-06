#This software was designed to deploy some keystrokes to automate SAP label printing
#Features
# Network socket to receive automated PLC printing packets
#Manual printing (same procedure but different triggers)
#
import time
import pyautogui
time.sleep(10)
 
# makes program execution pause for 10 sec
pyautogui.moveTo(1000, 1000, duration = 1)
 
# moves mouse to 1000, 1000.
pyautogui.dragRel(100, 0, duration = 1)
 
# drags mouse 100, 0 relative to its previous position,
# thus dragging it to 1100, 1000
pyautogui.dragRel(0, 100, duration = 1)
pyautogui.dragRel(-100, 0, duration = 1)
pyautogui.dragRel(0, -100, duration = 1)