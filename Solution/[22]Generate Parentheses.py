class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        stack = []
        def set_pair(left,right):
            if left == right == n:
                result.append(''.join(stack))
                return
            if left < n:
                stack.append('(')
                set_pair(left + 1, right)
                stack.pop()
            if right < left:
                stack.append(')')
                set_pair(left, right + 1)
                stack.pop()
        set_pair(0, 0)
        return result
                