import sys

dict = {
	"a" : 4,
	"b" : 7,
	"c" : 10,
}

def swap_unique_keys_values(dict):
	dict1 = {}
	a = []
	for k , v in list(dict.items()):
		a.append(v)
	for k , v in list(dict.items()):
		if a.count("v") == 1:
			dict1[k] = v
	new_dict = {v:k for  k,v in list(dict1.items())}
	return new_dict


if __name__ == "__main__":
	main()