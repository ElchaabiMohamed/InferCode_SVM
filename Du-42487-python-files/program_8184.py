my_dict = {"a" : 4, "b" : 7, "c" : 10}

def swap(my_dict):
	new_dict = {}
	new_dict = {v : k for (k,v) in list(my_dict.items())}
	return new_dict


def main():
	new_dict = swap(my_dict)
	for (k, v) in list(new_dict.items()):
		print((list(new_dict.items())))

if __name__ == '__main__':
	main()
