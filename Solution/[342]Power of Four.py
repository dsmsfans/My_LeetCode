class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        if n == 1:
            return True
        result = log(n , 4)
        return result - int(result) == 0
        