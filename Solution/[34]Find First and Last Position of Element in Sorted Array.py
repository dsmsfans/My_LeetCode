class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = [-1,-1]
        start = True
        end = True
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target and start:
                    output[0] = i
                    start = False
                if nums[len(nums) - 1 - i] == target and end:
                    output[1] = len(nums) - 1 - i
                    end = False
                if not start and not end:
                    return output
        else:
            return output