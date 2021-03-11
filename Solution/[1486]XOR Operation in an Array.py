class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        output = 0
        for i in range(start, start + n * 2, 2):
            output = output ^ i
        return output
        