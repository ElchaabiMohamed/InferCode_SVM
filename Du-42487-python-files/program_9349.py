def minimun(a):
	if len(a) == 1:
		return nums[0]
	
	mini = minimun(nums[:-1])

	if nums[-1] < mini:
		return nums[-1]
	else:
		return mini


def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()
