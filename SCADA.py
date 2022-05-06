#This script enables the PC to open SCADA successfully.
####
import pyautogui
import time
import os
import sys
pyautogui.FAILSAFE = True

#def My_Documents(location):
#	import ctypes.wintypes
#		#####-----This section discovers My Documents default path --------
#	CSIDL_PERSONAL = location       # My Documents
#	SHGFP_TYPE_CURRENT = 0   # Get current, not default value
#	buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
#	ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
#	#####-------- please use buf.value to store the data in a variable ------- #####
#	#add the text filename at the end of the path
#	temp_docs = buf.value
#	return temp_docs

#try to detect IE installation
#try #1: x86 files
#output
#mis_docs1 = My_Documents(42)
#ie_address86 = str(mis_docs1) + r"\Internet Explorer\iexplore.exe"
#try2: 64bit 
#mis_docs2 = My_Documents(38)
#ie_address64 = str(mis_docs2) + r"\Internet Explorer\iexplore.exe"
	#test if any of this exists
#if os.path.exists(ie_address86):
#	ie_address = ie_address86 
#	subprocess.run([ie_address])
#elif os.path.exists(ie_address64):
#	ie_address = ie_address64
#	subprocess.run([ie_address])
#else:
#	#show a message that there's no VLC installed
#	tkinter.messagebox.showwarning(title="Failed Action", message= f"Internet Explorer not detected")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

pyautogui.hotkey('win','r')
pyautogui.write('iexplore.exe')
pyautogui.press('enter')
time.sleep(10)
pyautogui.hotkey('winleft','up')
time.sleep(5)
pyautogui.press('f4')
pyautogui.write('10.65.64.27/startupcs.html')
pyautogui.press('enter')
time.sleep(10)
pyautogui.write('pantalla mtto')
pyautogui.press('tab')
pyautogui.write('mttopant')
pyautogui.press('enter')
time.sleep(10)
#locate Vision General button
scada_btn = pyautogui.locateOnScreen(resource_path(r"images/scadabutton.jpg"),grayscale=True, confidence=.5)
#center the button
button7point = pyautogui.center(scada_btn)
#divide button coordinates into x and y
button7x, button7y = button7point
pyautogui.click(button7x, button7y)

