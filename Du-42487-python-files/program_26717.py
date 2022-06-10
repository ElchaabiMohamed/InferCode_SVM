def get_price(age):

 	if int(age) <= 16:
 	  return '5' 
 	elif int(age) > 60:
 	  return '7'
 	else:
 	  return '10'


def merge_lists(l1,l2):
		newlist = []
		i = 0
		while i < len(l1):
			newlist.append(l1[i])
			i = i + 2

		j = 0
		while j < len(l2):
			newlist.append(l2[j])
			j = j + 2
		return newlist
