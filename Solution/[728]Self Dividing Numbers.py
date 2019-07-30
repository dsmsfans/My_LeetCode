class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left,right+1):
            for j in str(i):
                if j == '0':
                    break
                if i % int(j) != 0:
                    break
            else:
                result.append(i)
        return result