import sys

dict = {
	"a" : 4,
	"b" : 7,
	"c" : 10,
}

def swap_unique_keys_values(dict):
	for k in dict:
		print(k)
	new_dict = {v:k for  k,v in list(dict.items())}
	return new_dict


if __name__ == "__main__":
	main()