import tkinter.filedialog
import tkinter.messagebox

def encryptText(message):
	failmessage = ""
	table = str.maketrans(' \n\t', '¥§Ξ')
	messageInput = message.translate(table)

	rotor_input = [
'@', 'b', '¥', 'T', '2', '~', '=', 'm', '"', 'p',
'<', 'i', '$', 'c', '(', 'C', 'k', 'n', 'Y', 'G',
'u', ')', '/', 'W', 'o', ']', 'g', '+', '0', '*',
'#', 'P', 'Q', '&', 'A', 'a', 'X', '5', 'w', 'I',
'v', '^', '{', '_', '|', 'K', '>', 'z', '4', 'e',
'f', 'F', 'r', ';', 'U', 'j', 'q', 'B', '?', 't',
"'", 'l', 'E', 'y', '7', 'V', '-', 'h', 's', 'M',
'J', 'N', 'x', '!', ',', '3', 'Ξ', 'S', 'd', '6',
'L', '8', 'O', '\\', '}', 'Z', 'R', '§', 'D', '[',
'.', ':', '%', 'H', '1', '9'
]
	rotor_alpha = [
'9', '1', 'H', '%', ':', '.', '[', 'D', '§', 'R',
'Z', '}', '\\', 'O', '8', 'L', '6', 'd', 'S', 'Ξ',
'3', ',', '!', 'x', 'N', 'J', 'M', 's', 'h', '-',
'V', '7', 'y', 'E', 'l', "'", 't', '?', 'B', 'q',
'j', 'U', ';', 'r', 'F', 'f', 'e', '4', 'z', '>',
'K', '|', '_', '{', '^', 'v', 'I', 'w', '5', 'X',
'a', 'A', '&', 'Q', 'P', '#', '*', '0', '+', 'g',
']', 'o', 'W', '/', ')', 'u', 'G', 'Y', 'n', 'k',
'C', '(', 'c', '$', 'i', '<', 'p', '"', 'm', '=',
'~', '2', 'T', '¥', 'b', '@'
]
	hasil = ""

	for i in range(len(messageInput)):
		try:
			huruf_dapat = rotor_input.index(messageInput[i])
			hasil = hasil + rotor_alpha[huruf_dapat]
			geser = rotor_alpha.pop(0)
			rotor_alpha.insert(len(rotor_alpha) + 1, geser)

		except ValueError:
			if messageInput[i] == "\t":
				failmessage += "<Tab>"

			elif messageInput[i] == "\n":
				failmessage += "<Newline>"

			elif messageInput[i] == "\r":
				failmessage += "<Carriage Return>"

			elif messageInput[i] == " ":
				failmessage += "<Space>"

			else:
				failmessage += messageInput[i]

	if failmessage == "":
		return hasil
	else:
		tkinter.messagebox.showerror("Value Error", "[%s] Tidak dapat dienkripsi" % failmessage)
		return hasil

def decryptText(message):
	failmessage = ""

	rotor_input = [
'@', 'b', '¥', 'T', '2', '~', '=', 'm', '"', 'p',
'<', 'i', '$', 'c', '(', 'C', 'k', 'n', 'Y', 'G',
'u', ')', '/', 'W', 'o', ']', 'g', '+', '0', '*',
'#', 'P', 'Q', '&', 'A', 'a', 'X', '5', 'w', 'I',
'v', '^', '{', '_', '|', 'K', '>', 'z', '4', 'e',
'f', 'F', 'r', ';', 'U', 'j', 'q', 'B', '?', 't',
"'", 'l', 'E', 'y', '7', 'V', '-', 'h', 's', 'M',
'J', 'N', 'x', '!', ',', '3', 'Ξ', 'S', 'd', '6',
'L', '8', 'O', '\\', '}', 'Z', 'R', '§', 'D', '[',
'.', ':', '%', 'H', '1', '9'
]
	rotor_alpha = [
'9', '1', 'H', '%', ':', '.', '[', 'D', '§', 'R',
'Z', '}', '\\', 'O', '8', 'L', '6', 'd', 'S', 'Ξ',
'3', ',', '!', 'x', 'N', 'J', 'M', 's', 'h', '-',
'V', '7', 'y', 'E', 'l', "'", 't', '?', 'B', 'q',
'j', 'U', ';', 'r', 'F', 'f', 'e', '4', 'z', '>',
'K', '|', '_', '{', '^', 'v', 'I', 'w', '5', 'X',
'a', 'A', '&', 'Q', 'P', '#', '*', '0', '+', 'g',
']', 'o', 'W', '/', ')', 'u', 'G', 'Y', 'n', 'k',
'C', '(', 'c', '$', 'i', '<', 'p', '"', 'm', '=',
'~', '2', 'T', '¥', 'b', '@'
]
	hasil = ""

	for i in range(len(message)):
		try:
			huruf_dapat = rotor_input.index(message[i])
			hasil = hasil + rotor_alpha[huruf_dapat]
			geser = rotor_alpha.pop(0)
			rotor_alpha.insert(len(rotor_alpha) + 1, geser)

		except Exception:
			if message[i] == "\t":
				failmessage += "<Tab>"

			elif message[i] == "\n":
				failmessage += "<Newline>"

			elif message[i] == "\r":
				failmessage += "<Carriage Return>"

			elif message[i] == " ":
				failmessage += "<Space>"

			else:
				failmessage += message[i]

	table = str.maketrans('¥§Ξ', ' \n\t')
	messageInput = hasil.translate(table)

	if failmessage == "":
		return messageInput
	else:
		tkinter.messagebox.showerror("Value Error", "[%s] Tidak dapat didekripsi" % failmessage)
		return messageInput

def encryptStegnographyText():
	pass