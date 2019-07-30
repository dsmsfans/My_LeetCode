class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A:
            return None
        temp = []
        temp2 = []
        invert = [-1]*len(A[0])
        for array in A:
            temp.append(array[::-1])
        for a in temp:
            a = [x + y for x,y in zip(a,invert)]
            temp2.append(map(abs,a)) 
        return temp2
            
        