
import sys 

def get_price(age):
	 

	if int(age) < 16:
		return "5"
	elif int(age) > 60:
		return "7"
	else:
		return "10"


def merge_lists(l1,l2):
	i = 0
	while i < len(l2):
		l1.append(l2[i])
		i = i + 1

	i = 0
	while i < len(l1):
		if i % 2 == 1 and i != 0:
			l1.remove(l1[i])
		i = i + 1
	return l1	

		
def weird_case(some_str):
	a = []
	line = some_str.strip("\n").split(" ")
	i = 0
	while i < len(line):
		word = line[i]
		x = 0
		while x < len(word):
			a.append(word[x])
			x = x + 1
		a.append(" ")
		i = i + 1	
	del a[len(a) - 1]
	x = -1
	i = 0
	while i <len(a):
		if a[i] != " ":
			x = x + 1
		if x == 0 or x % 2 == 0:
		    a[i] =str(a[i].upper())
		i = i + 1
	return " ".join(a)	    	


