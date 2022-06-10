def swap_unique_keys_values(d):

	l = [ v for (k, v) in d]
	z= []
	for c in l:
		if l.count(c) == 1:
			z.append(c)
	
	d1 = {v : k for (k, v) in list(d.items()) if v in z}
	return(d1)
		





def main():
	pass

if __name__ == "__main__":
	main()