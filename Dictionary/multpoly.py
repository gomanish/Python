'''
for this function polynomial is representated like :  
Eg:
   3x4 - 17x2 - 3x + 5 
   can be written as
   [(3,4),(-17,2),(-3,1),(5,0)]
   '''

def  multpoly(p1,p2):
	poly={}
	for (a,b) in p1:
		for (c,d) in p2:
			(m,n)=(a*c,b+d)
			if n in list(poly.keys()):
				poly[n]=poly[n]+m
			else:
				poly[n]=m
	ni=list(poly.keys())
	ni.sort()
	ans=[]
	for a in ni[::-1]:
		if poly[a]!=0:
			ans.append((poly[a],a))
	return(ans)
  
'''
input : [(1,1),(-1,0)],[(1,2),(1,1),(1,0)]
output : [(1, 3),(-1, 0)]
Explanation : (x - 1) * (x^2 + x + 1) = x^3 - 1
'''
  
  
