import sys

dict = {
	"a" : 4,
	"b" : 7,
	"c" : 10,
}

def swap_unique_keys_values(dict):
	new_dict = {v:k for  k,v in list(dict.items())}
	return new_dict

def main():
	dict1 = {}
	a = []
	for k  in dict:
		print(k)

	#print(swap_unique_keys_values(dict1))

if __name__ == "__main__":
	main()