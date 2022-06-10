def swap_keys_values(d):
	new_dict = {v:k for (k,v) in list(d.items())}
	return new_dict

def main():
	d = {'a' : 4, 'b' : 7, 'c' : 10}
	new_dict = swap_keys_values(d)
	print((new_dict[4]))

if __name__ == "__main__":
	main()