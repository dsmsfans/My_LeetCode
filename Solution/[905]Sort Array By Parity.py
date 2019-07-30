class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return None
        B = []
        C = []
        for num in A:
            if num % 2 == 0:
                B.append(num)
            else:
                C.append(num)
        return(B+C)
            
        