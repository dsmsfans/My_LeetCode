class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        up = 0
        down = len(S)
        output = [] 
        for i in S:
            if i == 'I':
                output.append(up)
                up += 1
            elif i == 'D':
                output.append(down)
                down -= 1
        output.append(down)
        return output
                
        