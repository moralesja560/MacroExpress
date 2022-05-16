from win32com.client import Dispatch
import sys
from tkinter import messagebox
import os
import pyautogui
import time


image = pyautogui.screenshot()
image.save('testing2.png')