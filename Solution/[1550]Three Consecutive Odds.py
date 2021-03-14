class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        odd = []
        for num in arr:
            if num % 2 != 0:
                odd.append(num)
            elif num %2 == 0:
                odd = []
            if len(odd) >= 3:
                return True
        return False
        