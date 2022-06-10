def swap_unique_keys_values(d):
	swappedDict = {}
	for i in d:
		if d[i] in swappedDict:
			del (swappedDict[d[i]])
		else:
			swappedDict[d[i]] = i
	return swappedDict

 
def main():
 
	a = {
	1: "a",
	2: "b",
	3: "c",
	4: "c"
	}
	print((swap_unique_keys_values(a)))
 
if __name__ == "__main__":
	main()