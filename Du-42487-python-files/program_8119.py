#revision 
import time

def countdown(num):
	if num == 0:
		print("LIFT OFF!")
	else:
		print(num)
		countdown(num-1)
if __name__ == "__main__":
	print(num) 


def search(str,letter):
	if letter in str:
		return "True"
	else:
		return "False"

def index(str,letter,pos):
	if pos in len(str):
		return -1
	elif str[pos] in letter:
		return pos
	elif recursive in str:
		return 1
	else:
		return index(str,letter,pos+1)

def fibonacci(n):
	if n <= 1:
		return n
	elif n == 0:
		return 0
	else:
		return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
	print("testing countdown")
	countdown(10)

	print("testing search")
	print(search("test", "t"))
	print(search("test", "a"))

	print("testing index")
	print(index("test", "t", 0))
	print(index("test", "a", 0))

	print("testing fibonacci")
	print(fibonacci(5))