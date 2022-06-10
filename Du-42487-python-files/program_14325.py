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
   z = 0
   x= 0

   while i < n - i:
      x = i
      i = i+z
      z = x
   print(i)

