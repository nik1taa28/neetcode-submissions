class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        land=0

        def ex(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
                return
            if grid[r][c]=='0' or (r,c) in visited:
                return
            visited.add((r,c))
            ex(r+1,c)
            ex(r-1,c)
            ex(r,c+1)
            ex(r,c-1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='1' and (r,c) not in visited:
                    ex(r,c)
                    land+=1
        return land

