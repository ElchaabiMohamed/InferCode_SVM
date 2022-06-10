import sys
from pprint import pprint
from operator import itemgetter
from copy import deepcopy
d = {"a" : 4 , "b" : 7, "c" : 10}
 

  


  
def swap_keys_values(a):
	new_dict = {v:k for k, v in list(a.items())}
	
	#print (new_dict.items())
	#print(new_dict[4])
	#return(sorted(new_dict.items())) 
	#print ("{" + ", ".join("%r: %r" % (key, new_dict[key]) for key in sorted(new_dict)) + "}")
	pprint (new_dict)	

def main():
	if __name__ == "__main__":
		main()
		
		