import sys


def swap_keys_values(d):
   d2 = dict((v,k) for k,v in list(d.items()))
   return (d2)

def main():
   d = {"a" : 1, "b" : 2, "c" : 3}
   print((swap_keys_values(d)))


if __name__ == "__main__":
	main()