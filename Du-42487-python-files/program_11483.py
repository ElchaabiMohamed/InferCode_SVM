def countdown(i):
    while i > 0:
    	print (i)
    	i = i - 1
    if i == 0:
        print("LIFT OFF!")

def search(str,letter):
	if letter in str:
		return "True"
	else:
		return "False"

def index(str,letter):
	i = 0
	while i < len(str):
		if letter in str[i]:
			return i
			i = i + 1
		else:
			return "-1"