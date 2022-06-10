def main():
	my_dict = {'a': 4, 'b': 7, 'c': 10}
	print((swap_key_values(my_dict)))

def swap_key_values(my_dict):
	new_dict = {v:k for (k, v) in list(my_dict.items())}
	return sorted(new_dict.items())
   
if __name__ == '__main__':
	main()
