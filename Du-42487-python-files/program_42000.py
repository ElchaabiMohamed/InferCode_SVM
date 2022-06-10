def reverse_list(nums):
    if len(nums) == 0:
        new_nums = list()
        return new_nums
    new_nums = reverse_list(nums[1:])
    new_nums.append(nums[0])
    return new_nums


def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main() 