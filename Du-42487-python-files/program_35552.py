import time
def countdown(num):
	if int(num) == 1:
		print(num)
		print("LIFT OFF!")
	else:
		print(num)
		time.sleep(0.1)
		countdown(int(num)-1)
	print("LIFT OFF!")
#while num >=1:
	#	print num
		#time.sleep(0.1)
		#num = num - 1
	#print "LIFT OFF!"


def search(str,letter):
	for item in str:
		if item == letter:
			return True
	return False











	#loop 
	#if letter in str:
	#	print True
	#else:
	#	print False



