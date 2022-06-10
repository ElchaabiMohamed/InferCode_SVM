import sys

j = {}

def swap_unique_keys_values(d):
	for i in d:
		if d[i] in j:
			del j[d[i]]
		else:	
			j[d[i]] = i	
	return j


def main():
	d = {'a' : 4, 'b' : 7, 'c' : 7}
	for i in d:
		if d[i] in j:
			del j[d[i]]
		else:	
			j[d[i]] = i	
	print(j)

if __name__ == '__main__':
	main()