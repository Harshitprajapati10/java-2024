# No of Islands. 200

from collections import deque

def bfs(grid, i, j):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque()
    q.append((i, j))
    grid[i][j] = '0'  
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                # Mark as visited and add to the queue
                grid[nx][ny] = '0'
                q.append((nx, ny))
                
def numIslands(grid):
    if not grid:
        return 0   
    num_islands = 0   
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                bfs(grid, i, j)
                num_islands += 1
    
    return num_islands

# Example usage:
grid = [
    ["1","1","1","1","1"],
    ["1","1","0","1","0"],
    ["0","0","1","1","0"],
    ["0","0","0","0","1"]
]

print(numIslands(grid))  
