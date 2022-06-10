def get_price(age):
	if age <= 16:
		return '5'
	elif age >= 60:
		return '7'
	else:
		return '10'

def merge_lists(l1, l2):
	i = 0
	j = 0
	l3 = []
	while i < len(l1):
		if l1[i] in l1:
			l3.append(l1[i])
			i = i + 2
	while j < len(l2):
		if l2[j] in l2:
			l3.append(l2[j])
			j = j + 2

	return l3

def weird_case(some_str):
    sent = ""
    i = True 
    for words in some_str:
        if i:
            sent += words.upper()
        else:
            sent += words.lower()
        if words != ' ':
            i = not i
    return sent
