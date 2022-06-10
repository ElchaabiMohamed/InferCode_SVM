
def swap_unique_keys_values(d):
	return {v : k for (k, v) in list(d.items()) if v in list(d.values())}

def main():
	d = {
		"a": 4,
		"b": 3,
		"c": 4,
		"d": 7,
	}

	print((swap_unique_keys_values(d)))

if __name__ == "__main__":
	main()