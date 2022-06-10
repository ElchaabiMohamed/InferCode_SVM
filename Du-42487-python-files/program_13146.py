import sys
#a= [4,3,1,2]
#i = sys.stdin.readline(int())
#j= sys.stdin.readline(int())
def swap(a,i,j):

	tmp = a[j]
	a[j] = a[i]
	a[i] = tmp


def reverse(a):
	i=0
	j=len(a)-1	
	while j>len(a)/2:
		swap(a,i,j)
		i+=1
		j= j-1

#def main():
#	print swap(a,i,j)
##	print reverse(a)
	

#if __name__ == "__main__":
 #  main()
