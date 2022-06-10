import sys

def minimum(list=[]):
	if len(list) == 1:
		return list[0]
	max_value = max(list)
	return 	minimum(list.remove(max_value))

def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()