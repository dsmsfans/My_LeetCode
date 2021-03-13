class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        first_word = s[0]
        word = ''
        result = 0
        for i in s:
            if i == first_word:
                count += 1
                s = s + i
            if i != first_word:
                count -= 1
                s = s + i
            if count == 0:
                result += 1
                s = ''
        return result
            
        