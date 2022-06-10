def minimum(nums):

	if len(nums) == 1:
		return nums[0]



	smallest = minimum(nums[:-1])




	if nums[-1] < smallest:
		return nums[-1]
	else:
		return smallest