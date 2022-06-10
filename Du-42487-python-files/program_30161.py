import sys

def swap_keys_values(d):
	return {v:k for (k, v) in list(d.items())}

def main():
	d = {'cats':4, 'dogs':3}
	print((swap_keys_values(d)))

if __name__=="__main__":
	main()