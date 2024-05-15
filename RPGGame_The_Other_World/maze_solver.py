def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and maze[r][c] == 1 and not visited[r][c]

    def solve(r, c):
        if r == rows - 1 and c == cols - 1:
            return True
        visited[r][c] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc) and solve(nr, nc):
                return True
        visited[r][c] = False
        return False

    return solve(0, 0)


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
]

if solve_maze(maze):
    print("Maze solved!")
else:
    print("No solution found.")