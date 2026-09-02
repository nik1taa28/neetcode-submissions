class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea=0
        visited=set()
        def dfs(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
                return 0
            if grid[r][c]==0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c]==1:
                    area=dfs(r,c)
                    maxArea=max(maxArea,area)
        
        return maxArea