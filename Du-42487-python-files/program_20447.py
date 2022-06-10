def swap_unique_keys_values(d):

	new_d = {}

	a = list(set(d.values()) & set(d.values()))

	for (k,v) in list(d.items()):

		if v not in a:

			new_d[v] = k


	return new_d

def main():
	print((swap_unique_keys_values(d)))

if __name__ == "__main__":
	main()