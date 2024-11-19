import tkinter as tk
import tkinter.ttk as tt
import U_U
import O_O
import os

class SimpleServiceText(tk.Frame):
	"""docstring for ClassName"""
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.parent.title("Untitled - Simple Service Text")
		self.filename = None
		self.interface()
		self.menubar()
		self.prompt()

		self.parent.bind('<Escape>', self.exitSST)

		self.parent.bind('<F1>', self.passCommand)
		self.parent.bind('<F2>', self.passCommand)
		self.parent.bind('<F3>', self.encryptText)
		self.parent.bind('<F4>', self.decryptText)

		self.parent.bind('<F5>', self.passCommand)
		self.parent.bind('<F6>', self.passCommand)
		self.parent.bind('<F7>', self.passCommand)
		self.parent.bind('<F8>', self.passCommand)

		self.parent.bind('<F9>', self.passCommand)
		self.parent.bind('<F10>', self.passCommand)
		self.parent.bind('<F11>', self.passCommand)
		self.parent.bind('<F12>', self.passCommand)

		self.parent.bind('<Control-x>', self.cutText)

		self.parent.bind('<Control-c>', self.copyText)

		self.parent.bind('<Control-s>', self.saveText)

		self.parent.bind('<Control-Shift-s>', self.saveText)

		self.parent.bind('<Control-Shift-X>', self.executePrompt)
		self.parent.bind('<Control-Shift-V>', self.evaluatePrompt)

	def interface(self):
		self.Notebook = tt.Notebook(self.parent)
		self.Notebook.grid(row=0, column=0)

		self.fileFrame = tt.Frame(self.Notebook, width=400, height=280)
		self.promptFrame = tt.Frame(self.Notebook, width=400, height=280)

		self.fileFrame.pack(fill='both', expand=True)
		self.promptFrame.pack(fill='both', expand=True)

		self.Notebook.add(self.fileFrame, text='File Text')
		self.Notebook.add(self.promptFrame, text='Prompt')

		self.mainScreen = tk.Text(self.fileFrame, width=80, height=25, bg='#0f2830', fg='#00d37f', insertbackground='#f7f7f7')
		self.mainScreen.grid(row=0, column=0)

		self.mMenu = tk.Menu(self.parent)

		self.mScroll = tk.Scrollbar(self.fileFrame, orient='vertical', command=self.mainScreen.yview)
		self.mainScreen.configure(yscrollcommand=self.mScroll.set)
		self.mScroll.grid(row=0, column=1, sticky='ns')

	def menubar(self):
		self.parent.config(menu=self.mMenu)

		self.fileMenu = tk.Menu(self.mMenu, tearoff=0)

		self.fileMenu.add_command(label="New", command=self.newText)
		self.fileMenu.add_command(label="Open Normal", command=self.openText)
		self.fileMenu.add_command(label="Open Binary", command=self.openBinaryText)
		self.fileMenu.add_command(label="Save Normal", command=self.saveText)
		self.fileMenu.add_command(label="Save As", command=self.saveAsText)
		self.fileMenu.add_separator()
		self.fileMenu.add_command(label="Encrypt Text", command=self.encryptText)
		self.fileMenu.add_command(label="Decrypt Text", command=self.decryptText)
		self.fileMenu.add_separator()
		self.fileMenu.add_command(label="Open Decrypt", command=self.openDecryptText)
		self.fileMenu.add_command(label="Save Encrypt", command=self.encryptText)
		self.fileMenu.add_separator()
		self.fileMenu.add_command(label="Shutdown", command=self.shutDown)
		self.fileMenu.add_command(label="Exit", command=self.exitSST)

		self.promptMenu = tk.Menu(self.mMenu, tearoff=0)

		self.promptMenu.add_command(label="Execute", command=self.executePrompt)
		self.promptMenu.add_command(label="Evaluate", command=self.evaluatePrompt)
		self.promptMenu.add_separator()
		self.promptMenu.add_command(label="Clear Prompt", command=self.evaluatePrompt)

		self.editMenu = tk.Menu(self.mMenu, tearoff=0)

		self.editMenu.add_command(label="Cut", command=self.cutText)
		self.editMenu.add_command(label="Copy", command=self.copyText)
		self.editMenu.add_command(label="Paste", command=self.pasteText)

		self.aboutMenu = tk.Menu(self.mMenu, tearoff=0)

		self.aboutMenu.add_command(label="About", command=self.aboutAuthor)

		self.mMenu.add_cascade(label="Menu file", menu=self.fileMenu)
		self.mMenu.add_cascade(label="Edit", menu=self.editMenu)
		self.mMenu.add_cascade(label="Prompt", menu=self.promptMenu)
		self.mMenu.add_cascade(label="About", menu=self.aboutMenu)

	def prompt(self):
		self.mainPrompt = tk.Text(self.promptFrame, width=60, height=25, bg='#0f2830', fg='#00d37f', insertbackground='#f7f7f7')
		self.mainPrompt.grid(row=0, column=0)

		self.Info = tk.Text(self.promptFrame, width=20, height=25, bg='#f7f7f7', fg='#070707')
		self.Info.grid(row=0, column=1)
		self.Info.insert('end', "+\n-\nx\n:")
		self.Info.configure(state='disabled')

		self.pScroll = tk.Scrollbar(self.promptFrame, orient='vertical', command=self.mainPrompt.yview)
		self.mainPrompt.configure(yscrollcommand=self.pScroll.set)
		self.pScroll.grid(row=0, column=2, sticky='ns')

	def saveText(self, event=None):
		U_U.saveText(self.parent, self.mainScreen, self.filename)

	def saveAsText(self, event=None):
		U_U.saveAsText(self.parent, self.mainScreen, self.filename)

	def newText(self, event=None):
		U_U.newText(self.parent, self.mainScreen, self.filename)

	def openText(self, event=None):
		U_U.openText(self.parent, self.mainScreen, self.filename)

	def openDecryptText(self, event=None):
		U_U.openDecryptText(self.parent, self.mainScreen, self.filename)

	def openBinaryText(self):
		U_U.openBinaryText(self.parent, self.mainScreen, self.filename)

	def encryptText(self, event=None):
		U_U.encryptText(self.parent, self.mainScreen, self.filename)

	def decryptText(self, event=None):
		U_U.decryptText(self.parent, self.mainScreen, self.filename)

	def executePrompt(self, event=None):
		O_O.executePrompt(self.parent, self.mainPrompt)

	def evaluatePrompt(self, event=None):
		O_O.evaluatePrompt(self.parent, self.mainPrompt)

	def clearPrompt(self):
		self.mainPrompt.delete(1.0, 'end')

	def cutText(self, event=None):
		mainScreen.event_generate("<<Cut>>")

	def copyText(self, event=None):
		mainScreen.event_generate("<<Copy>>")

	def pasteText(self, event=None):
		mainScreen.event_generate("<<Paste>>")

	def shutDown(self, event=None):
		os.system('shutdown /p')

	def aboutAuthor(self, event=None):
		tk.messagebox.showinfo("About", "Creted by : Eyr Emath")

	def passCommand(self, event=None):
		pass

	def exitSST(self, event=None):
		self.quit()
		