def count_letters(inputed, counter=0):
	if inputed[:-1] == '':
		return counter
	if counter == 0:
		counter += 1
	return count_letters(inputed[:-1], counter + 1)

def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()