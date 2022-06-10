import sys

j = {}

def swap_keys_values(d):
	for i in d:
		j[d[i]] = i
		return j


def main():
	my_dict = {'a' : 4, 'b' : 7, 'c' : 10}
	for i in my_dict:
		j[my_dict[i]] = i
	print(j)

if __name__ == '__main__':
	main()