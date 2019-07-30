class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort() 
        if len(nums1) == 2:
            ans = float(nums1[0] + nums1[1]) / 2
            return ans
        if len(nums1) % 2 == 0:
            a = nums1[int(len(nums1) / 2 - 1)]
            b = nums1[int(len(nums1) / 2)]
            ans = float(a + b) / 2
            return ans
        else:
            return nums1[int(len(nums1) / 2)]