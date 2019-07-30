class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        U = 0
        D = 0
        L = 0
        R = 0
        if not moves:
            return None
        for i in moves:
            if i == 'U':
                U += 1
            if i == 'D':
                D -= 1
            if i == 'L':
                L += 1
            if i == 'R':
                R -= 1
        
        if (U + D) == 0 and (L + R) == 0:
            return True
        
        return False