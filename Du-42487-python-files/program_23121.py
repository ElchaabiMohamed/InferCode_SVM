import sys

def maximum(a):
	if len(a) == 1:
		return a[0]
	
	maxi = maximum(a[:-1])

	if a[-1] > maxi:
		return a[-1]
	else:
		return maxi

def main():
    max = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
    main()
