
def swap_keys_values(d):
	reversed_d = dict((v,k) for k,v in d.items())
	return reversed_d


def main():
	d = {
		"a": 4,
		"b": 3,
		"c": 2
	}

	print((swap_keys_values(d)))

if __name__ == "__main__":
	main()