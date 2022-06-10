def swap_unique_keys_values(d):
	b = {}
	return{v:k for k,v in list(d.items())}

def main():
	d = { 'a' : 4,'b':7, 'c':10,'d':7}
	print((swap_unique_keys_values(d)))

if __name__ == '__main__':
	main()