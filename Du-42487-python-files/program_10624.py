def swap_unique_keys_values(d):

	new_d = {}

	keys = list(set(d.keys()))
	values = list(set(d.values()))

	i = 0 

	while i < len(keys):		
		new_d[values[i]] = keys[i]

	return new_d


def main():
	print((swap_unique_keys_values(d)))

if __name__ == "__main__":
	main()