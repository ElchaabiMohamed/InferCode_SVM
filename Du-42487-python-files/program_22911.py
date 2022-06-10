def count_letters(s):
	if s == "":
		return 0
	elif s != "":
		s = s.split()
		total +=1
		return total + count_letters(s) 

