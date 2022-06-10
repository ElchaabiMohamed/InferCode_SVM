def fibonacci(n):
	i = 1
	l= [0,1]
	while i < n+1:
		l.append(l[i]+l[i-1])
		i += 1
	return l[-1]



def main():
    print((fibonacci(0)))
    print((fibonacci(1)))
    print((fibonacci(5)))
    print((fibonacci(8)))

if __name__ == '__main__':
    main()


	# 0,1,2,3,4,5, 6, 7, 8, 9,10,11
	# 1,1,2,3,5,8,13,21,34,55,89,144