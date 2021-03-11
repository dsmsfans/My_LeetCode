class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x = 0
        y = 0
        output = 0
        rock = set(map(tuple, obstacles))
        dx = 0
        dy = 1
        for i in commands:
            if i == -1:
		        dx, dy = dy, -dx
            elif i == -2:
		        dx, dy = -dy, dx
            for j in range(i):
                if(x + dx, y +  dy) in rock:
                    break
                x = x + dx
                y = y + dy
                output = max(output, x * x + y * y)
        return output
                    
        
        