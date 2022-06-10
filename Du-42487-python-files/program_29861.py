a = [4, 3, 1, 2]

def swap(a,i,j):
 	tmp = a[j]
 	a[j] = a[i]
 	a[i] = tmp
 	return a

def reverse(a):
	i = 0
	if a != str():

	   while i < len(a):
		   p = i
		   j = i + 1

		   while j < len(a):
			   if a[j] < a[p]:
				   p = j
			   j = j + 1

		   swap(a,i,p)
		   i = i + 1

	   return a

	if a == str():
		b= []
		i = 0

		while i < len(a):
			b.append(a[len(a)-i-1])
			print(b)
			i = i + 1

def main():
	print(swap(a,2,3))
	print(reverse(a))

if __name__ == "__main__":
   main()