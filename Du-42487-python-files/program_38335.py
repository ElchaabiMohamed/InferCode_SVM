import sys

def minimum(a):
	if len(a) == 1:
		return a[0]
	
	mini = minimum(a[:-1])

	if a[-1] < mini:
		return a[-1]
	else:
		return mini

