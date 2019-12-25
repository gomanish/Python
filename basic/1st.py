# Use for, .split() and if to create a statement that will print out words that start with 's':

st='Sam print only the words that start with s in this sentence'
world=[x for x in st.split() if x[0].lower()=='s' ]
for z in world:
	print(z)
