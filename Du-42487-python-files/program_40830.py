def sum_up_to(n):
	if n == 0:
		return 0

	return (n+ sum_up_to(n-1))