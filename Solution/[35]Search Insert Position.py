class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        elif target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            for i in range(1, len(nums)):
                if nums[i - 1] < target < nums[i]:
                    return i