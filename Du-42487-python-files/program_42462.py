def get_price(age):
	if age < 17:
		return "5"
	elif age > 60:
		return "7"
	else:
		return "10"

def merge_lists(l1,l2):
	l3 = []
	i = 0
	while i < len(l1):
		if i % 2 == 0:
			l3.append(l1[i])
		i = i + 1
	j = 0
	while j < len(l2):
		if j % 2 == 0:
			l3.append(l2[j])
		j = j + 1
	return l3

#def weird_case(some_str):
   #i = 0
   #new_str = ""
   #for char in some_str:
	#if i % 2 == 0:
		
def remove_zeros(list):
	i = 0
	for value in list:
		if value == 0:
			del value
	return list
	
	
	
	#return [value for value in list if value != 0]
	
if __name__ == '__main__':
   print('calling get_price(\'change\')')
   print(weird_case('change the case'))