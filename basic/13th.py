''' PAPER DOLL: Given a string, return a string wherefor every 
character in the original there are three characters'''

def paper_doll(text):
	m=""
	for chac in text:
		m=m+chac*3
	return m

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
