import sys

def minimum(list):
	if len(list) == 1:
		return list[0]
	elif list[0] < minimum(list[1:]):
		return list[0]
	

def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()