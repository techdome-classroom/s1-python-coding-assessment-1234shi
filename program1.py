class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
       def num_islands(grid):
    if not grid or not grid[0]:
        return 0
    
    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        # If the current cell is out of bounds or is water ('W'), return
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
            return
        
        # Mark the current land cell as visited by setting it to 'W'
        grid[r][c] = 'W'
        
        # Recursively visit the neighboring cells (up, down, left, right)
        dfs(r - 1, c)  # Up
        dfs(r + 1, c)  # Down
        dfs(r, c - 1)  # Left
        dfs(r, c + 1)  # Right
    
    island_count = 0
    
    # Iterate over each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we find an unvisited land cell ('L'), it means we found a new island
            if grid[r][c] == 'L':
                # Perform DFS to mark all connected land cells
                dfs(r, c)
                # Increment the island count
                island_count += 1
    
    return island_count

                    
        
