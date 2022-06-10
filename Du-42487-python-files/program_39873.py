def fibonacci(n):
	prev = 0
	cur = 1
	i = 0
	while i < n:
		tmp = cur
		cur = cur + prev
		prev = tmp
		i = i + 1
	return cur





def main():
    print((fibonacci(0)))
    print((fibonacci(1)))
    print((fibonacci(5)))
    print((fibonacci(8)))

if __name__ == '__main__':
    main()
