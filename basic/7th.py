''' ANIMAL CRACKERS: Write  function takes a two-word
string and returns true if both words begin with same 
letter'''
def animal_crackers(text):
	return(text.lower().split()[0][0]==text.lower().split()[1][0])

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
