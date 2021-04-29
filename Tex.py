from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def saveDoc():
	print("Saving input: \n" + inputValue)
	filepath = asksaveasfilename(defaultextension="txt")
	if not filepath:
		return
	with open(filepath, "w") as output_file:
		inputValue = notes.get(1.0, END)
		output_file.write(inputValue)

def openDoc():
	filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
	if not filepath:
		return
	notes.delete(1.0, END)
	with open(filepath, "r") as inputFile:
		text = inputFile.read()
		notes.insert(END, text)

def newDoc():
	print("New Document")
	notes.delete(1.0, END)

def closeApp():
	print("Closing")
	exit()

# make new window
root = Tk() 
controls = Frame(root, background='#3E4149')
controls.pack(anchor=NW, fill=BOTH)

# Set up window
root.title("Simple Text Editor") 
w = 400
h = 400
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
windo_x = (screen_w/2) - (w/2)
windo_y = (screen_h/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, windo_x, windo_y))

# make buttons
save_button = Button(controls, text="Save", highlightbackground='#3E4149', command = saveDoc)
save_button.pack(side=LEFT, anchor=NW)

open_button = Button(controls, text="Open", highlightbackground='#3E4149', command = openDoc)
open_button.pack(side=LEFT, anchor=NW)

newdoc_button = Button(controls, text="New", highlightbackground='#3E4149', command = newDoc)
newdoc_button.pack(side=LEFT, anchor=NW)

exit_button = Button(controls, text="Exit", highlightbackground='#3E4149', command = closeApp)
exit_button.pack(side=LEFT, anchor=NW)

# Make text field
scrollbar = Scrollbar(root) 
scrollbar.pack(side=RIGHT, fill=Y)
notes = Text(root, yscrollcommand=scrollbar.set, bd=1, height=w, width=h, bg="#0e1113", fg="#d5fbe3", insertbackground="#d5fbe3") 
notes.pack(fill=X, side=BOTTOM)
scrollbar.config(command=notes.yview) 


# Start!
root.mainloop() 