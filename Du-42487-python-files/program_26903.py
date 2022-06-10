def reverse_list(nums):
	if len(nums) == 0:
		n = list()
		return n

	

	n = reverse_list(nums[1:])
	n.append(nums[0])
	return n