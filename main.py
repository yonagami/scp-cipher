text = 'Hello World'
text[0] = 'B'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in text.lower():
		index = alphabet.find(char)
		print(char, index)
		new_index = index + shift
