import sys

def minimum(list=[]):
	if len(list) == 1:
		return list[0]
	max_value = max(list)
	print(max_value)

def main():
    minimum([6,5,1,3,4])
  
if __name__ == '__main__':
    main()