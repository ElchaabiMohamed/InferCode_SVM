def swap_unique_keys_values(d):
	return {v : k for (k, v) in list(d.items())}


def main():
	print((swap_unique_keys_values(d)))

if __name__ == "__main__":
	main()