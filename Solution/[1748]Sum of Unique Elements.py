class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num] = num
            else:
                dict1[num] = 0
        return sum(dict1.values())