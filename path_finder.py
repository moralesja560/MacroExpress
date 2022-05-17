#This function is very interesting. It discovers "My Documents" folder default path. 
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



for x in range(0, 70):
	print(f"{x} {My_Documents(x)}")
