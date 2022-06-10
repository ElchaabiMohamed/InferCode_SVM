def swap_unique_keys_values(d):

	z = []
	l = []
	for c in list(d.items()):
		l.append(c[1])
	for c in l:
		if l.count(c) == 1:
			z.append(c)
	
	d1 = {v : k for (k, v) in list(d.items()) if v in z}
	return(d1)
		





def main():
	pass

if __name__ == "__main__":
	main()