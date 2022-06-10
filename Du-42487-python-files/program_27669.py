def reverse_list(nums):
    if len(nums) == 0:
        return []

    return reverse_list(nums[1:]) + nums[:1]
