'''
The library at the Hogwarts School of Witchcraft and Wizardry has computerized its book issuing process. The relevant information
is provided as text from standard input in three parts: information about books, information about borrowers and information about
checkouts. Each part has a specific line format, described below.
    Information about books
    Line format: Accession Number~Title

    Information about borrowers
    Line format: Username~Full Name

    Information about checkouts
    Line format: Username~Accession Number~Due Date
    Note: Due Date is in YYYY-MM-DD format.

Assume that the data is internally consistent. For every checkout, there is a corresponding username and accession number in the input data,
and no book is simultaneously checked out by two people.
Python program to read the data as described above and store "output.txt file" details about books that have been checked out. 
Each line should describe to one currently issued book in the following format:  Due Date~Full Name~Accession Number~Title

Output should be sorted in increasing order of due date. For books due on the same date, sort in increasing order of full name.
If the due date and full name are both the same, sort based on the accession number, and, finally, the title of the book.
'''


fh=open("Input.txt","r")
book={}
borro={}
checkout=[]
temp=0

for line in fh.readlines():
	if line=='Books\n':
		temp=1
		continue
	elif line=='Borrowers\n':
		temp=2
		continue
	elif line=='Checkouts\n':
		temp=3
		continue
	if temp==1:
		(a,b)=line.split('~')
		book[a]=b[:-1]
	elif temp==2:
		(a,b)=line.split('~')
		borro[a]=b[:-1]
	else:
		if line=='EndOfInput':
			break
		checkout.append(line[:-1])
fh.close()


l=[]
for list in checkout:
	l.append(list.split('~')[::-1])

fh=open("Output.txt","w")
result=[]
for list in l:
	(d,b,s)=list
	result.append("{}~{}~{}~{}".format(d,borro[s],b,book[b]))

result.sort()
for x in result:
	fh.write(x)
	fh.write("\n")

fh.close()
