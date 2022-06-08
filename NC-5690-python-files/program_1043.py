def doubleLettre(mot):
	res=0
	for i in range(len(mot)):
		if mot[i]==mot[i-1]:
			res=1
	if res==1:
		return True
	if res==0:
		return False
			
