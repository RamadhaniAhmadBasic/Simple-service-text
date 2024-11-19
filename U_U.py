import os
import tkinter.filedialog
import tkinter.messagebox
import T_T

def saveText(parent, mainScreen, filename):
	if filename == None:
		filename = tkinter.filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt"), ("Eyr Encryption","*.eyr")])

		if filename == "":
			filename = None

		else:
			file = open(filename, "w", encoding='utf-8')
			file.write(mainScreen.get(1.0, 'end'))
			file.close()
			parent.title(os.path.basename(filename) + " - Simple Service Text")

def saveAsText(parent, mainScreen, filename):
	filename = tkinter.filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt"), ("Eyr Encryption","*.eyr")])
	file = open(filename, "w", encoding='utf-8')
	file.write(mainScreen.get(1.0, 'end'))
	file.close()
	parent.title(os.path.basename(filename) + " - Simple Service Text")

def newText(parent, mainScreen, filename):
	parent.title("Untitled - Simple Service Text")
	filename = None
	mainScreen.delete(1.0,'end')

def openText(parent, mainScreen, filename):
	filename = tkinter.filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt"), ("Eyr Encryption","*.eyr")])
	if filename == "":
		filename = None
	else:
		parent.title(os.path.basename(filename) + " - Simple Service Text")
		mainScreen.delete(1.0,'end')
		file = open(filename, "r", encoding='utf-8')
		mainScreen.insert(1.0, file.read())
		file.close()

def openDecryptText(parent, mainScreen, filename):
	filename = tkinter.filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt"), ("Eyr Encryption","*.eyr")])
	if filename == "":
		filename = None
	else:
		parent.title(os.path.basename(filename) + " - Simple Service Text")
		mainScreen.delete(1.0,'end')
		file = open(filename, "r", encoding='utf-8')
		mainScreen.insert(1.0, file.read())
		message = mainScreen.get(1.0, 'end').strip('\n')
		file.close()
		mainScreen.delete(1.0, 'end')
		mainScreen.insert('end', T_T.encryptText(message))

def openBinaryText(parent, mainScreen, filename):
	filename = tkinter.filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt"), ("Eyr Encryption","*.eyr")])
	if filename == "":
		filename = None
	else:
		parent.title(os.path.basename(filename) + " - Simple Service Text")
		mainScreen.delete(1.0,'end')
		file = open(filename, "rb")
		mainScreen.insert(1.0, file.read())
		file.close()

def encryptText(parent, mainScreen, filename):
	message = mainScreen.get(1.0, 'end').strip('\n')
	mainScreen.delete(1.0, 'end')
	mainScreen.insert('end', T_T.encryptText(message))

def decryptText(parent, mainScreen, filename):
	message = mainScreen.get(1.0, 'end').strip('\n')
	mainScreen.delete(1.0, 'end')
	mainScreen.insert('end', T_T.decryptText(message))