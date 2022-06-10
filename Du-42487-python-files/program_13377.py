def swap_unique_keys_values(d):

	d1 = {v : k for (k, v) in list(d.items()) if len(v) > 1}
	return(d1)




def main():
	pass

if __name__ == "__main__":
	main()