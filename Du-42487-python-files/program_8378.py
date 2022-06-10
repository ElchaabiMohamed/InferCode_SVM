import sys
from operator import itemgetter
from copy import deepcopy
d = {"a" : 4 , "b" : 7, "c" : 10} 


def swap_keys_values(a):
	l = []
	new_dict = {v:k for k, v in list(a.items())}
	
	#print (new_dict.items())
	#print(new_dict[4])
	return(sorted(new_dict.items()))
def main():
	if __name__ == "__main__":
		main()