def minimum(a):
	if len(a) == 1:
		return a[0]

	le = a[0:1]
	a = a[1:]
	if minimum(le)<minimum(a):
		return minimum(le)
	else:
		return minimum(a)

def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()
