def get_price(age):
	if int(age) <= 16:
	 	return "5"
	elif int(age) > 60:
		return "7"
	else:
		return "10"
def merge_lists(l1,l2):
	a = []
	i = 0
	while i < len(l1):
		a.append(l1[i])
		i = i + 2
	j = 0
	while j < len(l2):
		a.append(l2[j])
		j = j + 2
	return a

def weird_case(some_str):
	some_str = input().upper()
	parse = " ".join(some_str).split()
	sentence = ""
	a = ""
	b = []

	j = 0
	while j < len(some_str):
		#print string[j]
		if some_str[j] == " ":
			b.append(j)
		j = j + 1

	i = 0
	while i < len(parse):	
		if i % 2 == 0:
			a += parse[i] 
		elif i % 2 != 0:
			a += parse[i].lower()
		i = i + 1

	#print a
 

	counter = 0 
	k = 0
	while k < len(a):
		sentence += a[k]	
		if b[0] == k + 1:
			sentence  += " "
		if b[1] == k + 2:
			sentence += " "
		k = k + 1

	print(sentence)



def remove_zeros(a):
	i = 0
	while i < len(a):
		if a[i] == 0:
			del a[i]
		if a[i] == 0:
			del a[i]
		i = i + 1
	

