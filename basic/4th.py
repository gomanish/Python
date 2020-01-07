# Pig Latin problem

def piglatin(word):
	first_letter = word[0]
	if first_letter[0] in 'aeiou':
		pigword = word + 'ay'
	else:
		pigword = word[1:] + first_letter + 'ay'

	print(pigword)

''' if word start with vowel ,add 'ay' to end
if word do not start vowel ,put first letter at the end ,then add 'ay' '''



piglatin('apple') # function call
piglatin('word')  
