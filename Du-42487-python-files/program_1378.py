def swap_unique_keys_values():
	d1 = {v : k for (k, v) in list(d.items()) if d.count(v) == 1}
	return(d1)



def main():
	pass

if __name__ == "__main__":
	main()