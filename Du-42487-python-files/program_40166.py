def count_letters(s,i=0):
	i +=1
	if i == len(s):
		return 1
	if len(s) > 0:
		return 1  + count_letters(s, i)
	else:
		return 0
# from count_102 import count_letters

def main():
    # len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    # print(len("catastrophe"))
    print((count_letters('')))

if __name__ == '__main__':
    main()


# i(1) + (i)
# 2 + (i)