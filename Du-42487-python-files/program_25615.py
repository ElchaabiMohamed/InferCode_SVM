import sys

def swap_keys_values(d):
	new_dict = {v:k for (k,v) in list(d.items())}
	return new_dict

my_dict = {"a" : 4,
           "b" : 7,
           "c" : 10
           }
def main():
	print((swap_keys_values(my_dict)))

if __name__ == "__main__":
	main()
   
