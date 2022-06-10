import sys
from pprint import pprint
d = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
  
def swap_keys_values(a):
	new_dict = {v:k for k, v in list(a.items())}
	l = []
	for i in a:
		l.append(a[i])
	#print(l)	
	for i in l:
		#print(l.count(i))
		if l.count(i) > 1:
			del new_dict[i]
			break
	return (new_dict)		
	
	
	
	return (new_dict)	
	
	
def main():
	if __name__ == "__main__":
		main()
		
swap_keys_values(d)
