import time

def countdown(num):
	i = 0
	while i < int(num):
		return int(num) - 1
		i = i + 1


def search(str, letter):
	if letter in str:
		return "True"
	else:
		return "False"

def index(str, letter):
	if letter in str:
		return str.find(letter)
	else:
		return "-1"