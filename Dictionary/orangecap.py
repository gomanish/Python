'''Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score.
Your function should return a pair (playername,topscore) where playername is a string, the name of the player with the highest score, 
and topscore is an integer, the total score of playername.
'''

def orangecap(l):
	r={}
	for x in list(l.keys()):
		for y in list(l[x].keys()):
			if y in list(r.keys()):
				r[y]=r[y]+l[x][y]
			else:
				r[y]=l[x][y]

	max=0
	for x in list(r.keys()):
		if max<r[x]:
			ans=(x,r[x])
			max=r[x]

	return(ans)
  
  
  print(orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}))
  
  '''
  output : ('player3', 100)
  '''
  
  
