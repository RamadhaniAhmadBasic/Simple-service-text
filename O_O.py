import tkinter.filedialog
import tkinter.messagebox

def executePrompt(parent, prompt):
	hasil = None
	command = prompt.get(1.0, 'end').rstrip('\n')
	try:
		hasil = exec(command)
	except Exception as e:
		tkinter.messagebox.showerror("Can't Execute Prompt", "Maybe your syntaxt is incorrect, try to debug it")
	
	prompt.delete(1.0, 'end')
	try:
		prompt.insert('end', hasil)
	except UnboundLocalError:
		prompt.insert('end', 'Executed')
		
	

def evaluatePrompt(parent, prompt):
	parent
	command = prompt.get(1.0, 'end').rstrip('\n')
	try:
		hasil = eval(command)
	except Exception as e:
		tkinter.messagebox.showerror("Can't Evaluate Prompt", "Maybe your syntaxt is incorrect, try to debug it")
	
	prompt.delete(1.0, 'end')
	prompt.insert('end', hasil)