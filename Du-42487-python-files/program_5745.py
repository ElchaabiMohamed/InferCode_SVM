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
	print((swap_keys_values(dict)))

if __name__ == "__main__":
	main()