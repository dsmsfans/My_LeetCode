class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) %2 != 0:
            return False
        stack = []
        for p in s:
            if p == '[' or p == '{' or p == '(':
                stack.append(p)
            else:
                if not stack:
                    return False
                elif p == ']' and stack[-1] != '[':
                    return False
                elif p == '}' and stack[-1] != '{':
                    return False
                elif p == ')' and stack[-1] != '(':
                    return False
                stack.pop()
        if stack:
            return False
        else:
            return True
                
                    
            