def minesweeper(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def count_mines(r, c):
        return sum(1 for dr, dc in directions if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == '#')

    return [['#' if grid[r][c] == '#' else str(count_mines(r, c)) for c in range(cols)] for r in range(rows)]

# Example usage:
grid = [
    ["-", "#", "-"],
    ["-", "-", "#"],
    ["#", "-", "-"]
]

result = minesweeper(grid)
for row in result:
    print(" ".join(row))
