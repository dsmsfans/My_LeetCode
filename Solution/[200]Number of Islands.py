class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        total = 0
        def dfs(x,y):
            grid[x][y] = '0'
            if 0 <= (x - 1) < len(grid) and grid[x - 1][y] == '1':
                dfs(x - 1,y)
            if 0 <= (x + 1) < len(grid) and grid[x + 1][y] == '1':
                dfs(x + 1,y)
            if 0 <= (y - 1) < len(grid[0]) and grid[x][y - 1] == '1':
                dfs(x,y - 1)
            if 0 <= (y + 1) < len(grid[0]) and grid[x][y + 1] == '1':
                dfs(x,y + 1)
            return
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    total += 1
        return total