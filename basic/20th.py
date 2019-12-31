# anagram Check

def anagram(text1,text2):
	text1=''.join(text1.lower().split())
	text2=''.join(text2.lower().split())

	if len(text1) != len(text2):
		return False

	temp ={}

	for k in text1:
		if k in temp:
			temp[k] +=1
		else:
			temp[k]=1

	for k1 in text2:
		if k1 in temp:
			temp[k1] -= 1
		else:
			temp[k1]=1

	for k in temp:
		if temp[k] !=0:
			return False
	
	return True


te1=raw_input('Enter First word : ')
te2=raw_input('Enter Second word : ')
if anagram(te1,te2):
	print(te1+ ' is anagram of '+te2)
else:
	print(te1+ ' is not anagram of '+te2)
