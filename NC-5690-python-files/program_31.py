def doubleLettre(mot):
	res=0
	for l in mot:
		prec=''
		act=l
		if prec==act:
			res=1
	if res==1:
		return True
	else:
		return False
			
