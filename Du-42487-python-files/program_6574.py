import sys

def minimun(a):
	if len(a) == 1:
		return a[0]
	
	mini = minimun(a[:-1])

	if a[-1] < mini:
		return a[-1]
	else:
		return mini


def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()
