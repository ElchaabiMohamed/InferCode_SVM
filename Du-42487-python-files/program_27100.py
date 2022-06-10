import time
def countdown(num):
	if int(num) == 1:
		print(num)
		print("LIFT OFF!")
	else:
		print(num)
		time.sleep(0.1)
		countdown(int(num)-1)



def search(str,letter):
	for item in str:
		if item == letter:
			return True
	return False





def index(str,letter):
	i = 0 
	while i < len(str):
		if str[i] == letter:
			return i 
		i = i + 1
	return "-1"


	#loop 
	#if letter in str:
	#	print True
	#else:
	#	print False



