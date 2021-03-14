class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        
        peak = False
        for i in range(1,len(arr)):
            if not peak and arr[i - 1] < arr[i]:
                continue
            elif not peak and arr[i - 1] > arr[i] and (i-1) != 0:
                peak = True
                continue
            if peak and arr[i - 1] > arr[i]:
                continue
            else:
                return False
            
        return peak
        