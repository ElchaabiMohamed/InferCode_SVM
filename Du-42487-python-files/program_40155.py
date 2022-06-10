def minimum(a):
	i = 1
	mini = a[0]
	while i < len(a):
		 if mini < a[i]:
		 	mini = mini
		 elif mini > a[i]:
		 	mini = a[i]
		 i += 1
	return(mini)
