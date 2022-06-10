def swap_unique_keys_values(d):

	z = []
	for c in list(d.items()):
		z.append(c[1])
	
	d1 = {v : k for (k, v) in list(d.items()) if v in z}
	return(d1)
		





def main():
	pass

if __name__ == "__main__":
	main()