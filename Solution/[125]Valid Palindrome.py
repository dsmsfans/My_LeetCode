class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        result = [i for i in s if i.isalnum()]
        if result == result[::-1]:
            return True
        else:
            return False
        