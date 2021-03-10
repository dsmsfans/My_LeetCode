class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        number = str(n)
        p = 1
        total = 0
        for i in number:
            p = p * int(i)
            total = total + int(i)
        return p - total
        