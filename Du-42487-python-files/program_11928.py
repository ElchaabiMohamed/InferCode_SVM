import sys

dict = {
	"a" : 4,
	"b" : 7,
	"c" : 10,
}

def swap_keys_values(dict):
	new_dict = {v:k for  k,v in list(dict.items())}
	return new_dict

def main():
	dict1 = {}
	for k , v in list(dict.items()):
		if v not in dict1:
			dict1[k] = v
		else:
			pass
	print((swap_keys_values(dict1)))

if __name__ == "__main__":
	main()