import sys

def swap_keys_values(d):
	return {v: k for k, v in list(d.items())}

def main():
	print((swap_keys_values(sys.argv[1])))

if __name__ == '__main__':
	main()





