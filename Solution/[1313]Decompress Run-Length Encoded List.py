class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for n in range(0,len(nums),2):
            count = nums[n]
            while count > 0:
                output.append(nums[n + 1])
                count -= 1
        return output
            