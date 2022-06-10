def swap_unique_keys_values(d):
	lst = [x for x in list(d.values())]
	new_dict = {v:k for (k,v) in list(d.items()) if lst.count(v) == 1}
	return new_dict

def main():
	d = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
	new_dict = swap_unique_keys_values(d)
	print(new_dict)

if __name__ == "__main__":
	main()