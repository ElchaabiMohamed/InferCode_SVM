def swap_keys_values(dictionary):
	new_dictionary = {}
	for key in dictionary:
		new_dictionary[dictionary[key]] = key

	return new_dictionary

def main():
	test = {
	"a" : "A",
	"b" : "B",
	"c" : "C",
	}

	test_reverse = swap_keys_values(test)

	print((test_reverse["C"]))



if __name__ == '__main__':
	main()
