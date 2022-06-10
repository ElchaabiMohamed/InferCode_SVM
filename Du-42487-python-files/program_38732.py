def count_letters(str):
	total=0
	for letters in str:
		total+=1
	return total

def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()
