class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return None
        B = []
        for number in A:
            B.append(abs(number) ** 2)
        B.sort()
        return B
        