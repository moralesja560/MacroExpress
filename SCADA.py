#This script enables the PC to open SCADA successfully.
#
import pyautogui
import time
import subprocess
import tkinter
import os
pyautogui.FAILSAFE = True

def My_Documents(location):
	import ctypes.wintypes
		#####-----This section discovers My Documents default path --------
	CSIDL_PERSONAL = location       # My Documents
	SHGFP_TYPE_CURRENT = 0   # Get current, not default value
	buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
	ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
	#####-------- please use buf.value to store the data in a variable ------- #####
	#add the text filename at the end of the path
	temp_docs = buf.value
	return temp_docs

#try to detect IE installation
#try #1: x86 files
#output
mis_docs1 = My_Documents(42)
ie_address86 = str(mis_docs1) + r"\Internet Explorer\iexplore.exe"
#try2: 64bit 
mis_docs2 = My_Documents(38)
ie_address64 = str(mis_docs2) + r"\Internet Explorer\iexplore.exe"
	#test if any of this exists
if os.path.exists(ie_address86):
	ie_address = ie_address86 
	subprocess.run([ie_address])
elif os.path.exists(ie_address64):
	ie_address = ie_address64
	subprocess.run([ie_address])
else:
	#show a message that there's no VLC installed
	tkinter.messagebox.showwarning(title="Failed Action", message= f"Internet Explorer not detected")

time.sleep(5)
pyautogui.hotkey('winleft','up')
time.sleep(1)
pyautogui.press('f4')
pyautogui.write('10.65.64.27/startupcs.html')
pyautogui.press('enter')
time.sleep(10)
pyautogui.write('pantalla mtto')
pyautogui.press('tab')
pyautogui.write('mttopant')
pyautogui.press('enter')
pyautogui.keyUp('win')


