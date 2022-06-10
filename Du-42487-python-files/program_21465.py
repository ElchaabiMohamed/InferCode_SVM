import sys

def swap_keys_values(d):
	{v: k for k, v in list(d.items())}
 
def main():
	print((swap_keys_values(sys.stdin)))

if __name__ == '__main__':
	main()