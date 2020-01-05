# Reverse String 

def reverse(s):
	if len(s)<=1:
		return s
	return s[-1]+reverse(s[0:len(s)-1])


print reverse('My name is manish kumar')
print reverse('123456789')
