def minimum(a):
	if len(a)==1:
		return a[0]
	head=a[0]
	tail=a[1:]
	mintail=minimum(tail)
	if head>mintail:
		smallest=mintail
	else:
		smallest=head
	return smallest