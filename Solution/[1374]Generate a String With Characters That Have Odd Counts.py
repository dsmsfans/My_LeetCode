class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        return "a"*n if n % 2 != 0 else "a"+"b"*(n-1)
    
        