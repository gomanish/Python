''' OLD MACDONALD: Write a function that capitalizes the first 
and fourth letters of a name'''

def old_macdonald(name):
	return(name[:3].capitalize()+name[3:].capitalize())


print(old_macdonald('macdonald'))
print(old_macdonald('manish'))
