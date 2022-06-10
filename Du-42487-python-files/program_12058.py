def maximum(nums):
    if len(nums) == 1:
        return nums[0]
    maximum_num = maximum(nums[:-1])
    if nums[-1] > maximum_num:
        return nums[-1]
    else:
        return maximum_num


def main():
    max = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
    main()