import time
def countdown(num):
	if num == 1:
		print(num)
		print("LIFT OFF!")
	else:
		print(num)
		time.sleep(0.1)
		countdown(num-1)

#search function
def search(str, letter):
	for item in str:
		if item == letter:
			return True
	return False

#index function
def index(str, letter):
	i = 0 
	while i < len(str):
		if str[i] == letter:
			return i 
		i = i + 1
	return -1

#fibonacci function
def fibonacci(n):
   i = 1
   j = 0
   k = 0

   while i < n - i:
      k = i
      i = j + i
      j = k
   print(i)

