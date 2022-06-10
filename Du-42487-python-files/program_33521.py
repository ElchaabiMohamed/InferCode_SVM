def swap_unique_keys_values(d):

	new_d = {}

	for (key,value) in list(d.items()):
		
		if value not in list(d.values()):

			new_d[value] = key

	return new_d


def main():
	print((swap_unique_keys_values(d)))

if __name__ == "main":
	main()