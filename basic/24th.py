# Unique Characters in string

def uni_char(s):
	m=set()
	for k in s:
		if k in m:n
			return False
		else:
			m.add(k)
	return True

print(uni_char('abcde'))
print(uni_char('aabcde'))
