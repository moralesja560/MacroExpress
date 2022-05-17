#this script will automatically install a chrome extension called IETab.
#Corporate machines need this to open SCADA web dashboard

#detect if chrome is installed.
from win32com.client import Dispatch
import sys
from tkinter import messagebox
import os
import pyautogui
import time

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


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def get_version_via_com(filename):
    parser = Dispatch("Scripting.FileSystemObject")
    try:
        version = parser.GetFileVersion(filename)
    except Exception:
        return None
    return version

if __name__ == "__main__":
	appdata_path = f"{My_Documents(28)}\Google\Chrome\Application\chrome.exe"
	print(appdata_path)
	paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", appdata_path]
	#Try call the function
	try:
		version = list(filter(None, [get_version_via_com(p) for p in paths]))[0]
	except IndexError:
		messagebox.showerror(title="Error al encontrar Chrome", message="No hemos podido encontrar Chrome ¿Está instalado?")
		sys.exit() 
	#Generic exception
	except Exception as e:
		messagebox.showerror(title="Error desconocido", message={e})
		sys.exit()  
	else:
		print(version)

#information:
installRoute = messagebox.askyesno(title="Seleccione una Opción", message="Seleccione SI para abrir SCADA, NO para instalar IEtabHelper",)


pcSpeed = messagebox.askyesno(title="Modificación de Velocidad de Script", message="¿Esta es una pc rápida? Selecciona NO para esperar hasta 20 segundos para abrir chrome",)

if pcSpeed == True:
	sleepTime = 9
else:
	sleepTime = 40

if installRoute == False:
	#False es para Instalar IETabHelper.
	#open chrome
	pyautogui.hotkey('win','r')
	pyautogui.write('chrome.exe https://chrome.google.com/webstore/detail/ie-tab/hehijbfgiekmjfkfjpbkbammjbdenadd')
	pyautogui.press('enter')
	#sleep until chrome opens.
	time.sleep(sleepTime)
	#locate install button

	try:
		add_btn = pyautogui.locateOnScreen(resource_path(r"images/chromeInstall.jpg"),grayscale=True, confidence=.9)
	except:
		#if it fails
		messagebox.showerror(title="Error", message="No se encontró el botón para instalar la extensión ¿Hay internet?")
		sys.exit()
	else:
		time.sleep(sleepTime)
		#center the button
		button7point = pyautogui.center(add_btn)
		#divide button coordinates into x and y3
		button7x, button7y = button7point
		pyautogui.click(button7x, button7y)
	time.sleep(sleepTime)
	try:
		install_btn = pyautogui.locateOnScreen(resource_path(r"images/chromeclick.png"),grayscale=True, confidence=.9)
	except:
		#if it fails
		messagebox.showerror(title="Error", message="No se encontró el botón para instalar la extensión ¿Hay internet?")
		sys.exit()
	else:
		time.sleep(sleepTime)
		#center the button
		print(install_btn)
		#put an error catcher here.
		button7point = pyautogui.center(install_btn)
		#divide button coordinates into x and y3
		button7x, button7y = button7point
		pyautogui.click(button7x, button7y)
		#continue the script by installing the ietabhelper.
		

