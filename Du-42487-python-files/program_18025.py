import sys

def swap_unique_keys_values(d):
	keys = []
	new_d = {}
	old_vals = list(d.values())
	unique_vals = [v for v in old_vals if old_vals.count(v) < 2]
	for (k,v) in list(d.items()):
		if v in unique_vals:
			keys.append(k)
	#print(keys)
	#print(unique_vals)
	new_keys = unique_vals
	new_vals = keys
		

	y = 0
	for x in new_keys:
		new_d[x] = new_vals[y]
		y = y + 1
	return (new_d)



#def main():
#	d = {
#	"a" : 4,
#	"b" : 6,
#	"c" : 7,
#	"d" : 7,
#	}
#
#	swap_unique_keys_values(d)
#
#if __name__ == '__main__':
#	main()


		
		

