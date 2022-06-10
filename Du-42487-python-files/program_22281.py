def maximum(nums):

	

	if len(nums) == 1:
		return nums[0]

	topper = maximum(nums[:-1])

	

	if nums[-1] > topper:
		return nums[-1]
	else:
		return topper
