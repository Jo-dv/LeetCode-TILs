class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.grid = None
        self.visited = None
        self.answer = 0

    def search(self, row, col, val, step):
        if 0 <= row < self.m and 0 <= col < self.n and val < self.grid[row][col] and not self.visited[row][col]:
            self.answer = max(self.answer, step)
            self.visited[row][col] = True
            self.search(row - 1, col + 1, self.grid[row][col], step + 1)
            self.search(row, col + 1, self.grid[row][col], step + 1)
            self.search(row + 1, col + 1, self.grid[row][col], step + 1)
        return

    def maxMoves(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        self.visited = [[False] * self.n for _ in range(self.m)]
        for row in range(self.m):
            self.search(row, 0, -1, 0)
        
        return self.answer