def minimum(collection, itera=0, mini=None):
	if itera == 0:
		mini = collection[0]
	if len(collection) == itera:
		return mini
	if mini < collection[itera]:
		mini = collection[itera]
		return minimum(collection, itera + 1, mini)
	else:
		return minimum(collection, itera + 1, mini)


def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()