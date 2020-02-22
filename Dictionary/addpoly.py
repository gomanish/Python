'''
for this function polynomial is representated like :  
Eg:
   3x4 - 17x2 - 3x + 5 
   can be written as
   [(3,4),(-17,2),(-3,1),(5,0)]
'''

def addpoly(p1,p2):
	poly={}
	for (a,b) in p1:
		poly[b]=a
	
	for (a,b) in p2:
		if b in list(poly.keys()):
			poly[b]=poly[b]+a
		else:
			poly[b]=a
	ans=[]
	ni=list(poly.keys())
	ni.sort()
	for a in ni[::-1]:
		if poly[a]!=0:
			ans.append((poly[a],a))
	return(ans)
  
  '''
input : addpoly([(4,3),(3,0)],[(-4,3),(2,1)])

output : [(2, 1),(3, 0)]

Explanation : (4x^3 + 3) + (-4x^3 + 2x) = 2x + 3
'''
