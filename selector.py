# import all components
# from the tkinter library
from tkinter import *
 
# import filedialog module
from tkinter import filedialog
f = open("map.txt", "w")
 
counter=0
 
# Function for opening the 
# file explorer window
def browseFiles():
	global counter
	filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
                                        multiple=True,
										filetypes = (("Text files",
														"*.txt*"),
													("all files",
														"*.*",)))
 
	# Change label contents
	print(filename)
	# shoud untuple file names? 
	untuple = type(filename) is tuple
	if(untuple):
		for x in filename:
			f.write(x + '\n')
			##print(x)
			counter=(counter+1)
	else:
		f.write(filename + '\n')
		counter=(counter+1)
	label_file_explorer.configure(text="Files Opened = "+ str(counter))
 
def exitingSafe():
    f.close()
    quit()
 
 
 
# Create the root window
window = Tk()
 
# Set window title
window.title('')
 
# Set window size
window.geometry("150x200")
 
#Set window background color
window.config(background = "white")
 
button_explore = Button(window, 
						text = "Add Files",
						command = browseFiles) 
 
button_exit = Button(window, 
					text = "Exit",
					command = exitingSafe) 
 
label_file_explorer = Label(window, 
                            text = "Files Opened = 0",
                            width = 100, height = 4, 
                            fg = "red")
 
label_file_explorer.pack()
 
button_explore.pack(padx=10,pady=5)
 
button_exit.pack(padx=10,pady=5)
 
# Let the window wait for any events
window.mainloop()
