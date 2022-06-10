def swap_unique_keys_values(d):

	d = list(d.items())
	l = [ (v, k) for (k, v) in d if d.count(c[1]) == 1]
	print(l)

		





def main():
	pass

if __name__ == "__main__":
	main()