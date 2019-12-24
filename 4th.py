# Pig Latin problem

def piglatin(word):
	first_letter = word[0]
	if first_letter[0] in 'aeiou':
		pigword = word + 'ay'
	else:
		pigword = word[1:] + first_letter + 'ay'

	print(pigword)

''' if a word starts with a vowel, add 'ay' to end
if the word does not start with a vowel, put the first letter at the end, then add 'ay' '''



piglatin('apple') # function call
piglatin('word')  
