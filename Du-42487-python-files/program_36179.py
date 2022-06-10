def minimum(x):
	if len(x) == 1:
		return x[0]
	else:
		n, m = x[0] , minimum(x[1:])
	if n < m:
		return n
	else: 
		return m





def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()