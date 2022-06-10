def swap_unique_keys_values(d):

	new_d = {}

	keys = list(set(d.keys()))
	values = list(set(d.values()))

	print((keys, values))

def main():
	print((swap_unique_keys_values(d)))

if __name__ == "__main__":
	main()