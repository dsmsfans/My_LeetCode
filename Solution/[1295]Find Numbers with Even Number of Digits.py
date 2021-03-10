class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                total = total + 1
        return total
        