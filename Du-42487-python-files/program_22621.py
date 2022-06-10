import sys


def swap_unique_keys_value(dictionary):
	values = []
	new_dict = {}

	for key in dictionary:
		values.append(dictionary[key])

	for key, value in list(dictionary.items()):
		if values.count(value) == 1:
			new_dict[value] = key

	return new_dict

def main():
	test = {
	"a": "1",
	"b": "3",
	"c": "3",
	}

	new_dict = swap_unique_keys_value(test)
	print((list(new_dict.items())))	

if __name__ == '__main__':
	main()