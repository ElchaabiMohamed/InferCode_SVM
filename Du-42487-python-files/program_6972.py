def power(m, n):
	if n == 0:
		return 1
	elif n == 1:
		return m
	else:
		return m * power(m, n-1)

def main():
	m = 2
	n = 4
	print((power(m, n)))

if __name__=="__main__":
	main()
