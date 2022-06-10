import sys

def maximum(list):
	if len(list) == 1:
		return list[0]
	elif list[0] > maximum(list[1:]):
		return list[0]
	else:
		return maximum(list[1:])	
	

def main():
    max = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
    main()