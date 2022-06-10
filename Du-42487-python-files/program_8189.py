import sys

def swap_keys_values(d):
   a = {}
   for k, v in list(d.items()):
      a[v] = k
   return a


if __name__ == '__main__':
	main()
   