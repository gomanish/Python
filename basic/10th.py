''' MASTER YODHA: Given a sentence, return with the words reversed'''

def master_yodha(text):
	return(" ".join(text.split()[::-1]))

print(master_yodha('I am home'))
print(master_yodha('We are ready'))
