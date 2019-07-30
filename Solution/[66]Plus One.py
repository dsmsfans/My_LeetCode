class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        total = 0
        length  = len(digits)
        output = []
        for i in range(length):
            total += digits[i] * (10 ** (length - i - 1))
        total  = total + 1
        for i in str(total):
            output.append(i)
        
        return output
            