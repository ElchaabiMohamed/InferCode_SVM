
def fibonacci(n):

	num_one = 0
	num_two = 1
	i = 0
	while i < n:
		num_two = num_two + num_one
		num_one = num_two - num_one
		i = i + 1

	return num_two