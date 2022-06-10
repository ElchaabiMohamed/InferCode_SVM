
def minimum(a):
	i=1
	s=a[0]
	while i < len(a):
		if s > a[i]:
			s=a[i]
		i=i+1
	return(s)

def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()