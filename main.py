text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key, direction):
		key_index = 0
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		final_message = ''
		for char in message.lower():
				#Append space to the message
				if char == ' ':
						final_message += char
				else:
            #Find the right key character to encode
						key_char = key[key_index % len(key)]
						key_index += 1
						#Define the offset and the encrypted letter
						offset = alphabet.index(key_char);
						index = alphabet.find(char)
						new_index = (index + offset * direction) % len(alphabet) 
						final_message += alphabet[new_index]
		return final_message

encryption = vigenere(text, custom_key, 1)
print(encryption)
decryption = vigenere(encryption, custom_key, -1)
print(decryption)
