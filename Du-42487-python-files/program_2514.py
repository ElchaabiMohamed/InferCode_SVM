def maximum(nums):
    if len(nums) == 1:
        return nums[0]

    if nums[-1] < nums[-2]:
        return maximum(nums[:-1])
    else:
        return maximum(nums[:-2] + nums[-1:])
