text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''
for char in text.lower():
		if char == ' ':
				print('space!')
		index = alphabet.find(char)
		new_index = index + shift
		encrypted_text += alphabet[new_index]
		print('char:',char, 'encrypted text:',encrypted_text)
