m, n = 1, 1
mines = []
ans_mines = []
temp = ""
ans_count = 0

def search(grid, r, c):
    count = 0
    rows, cols = len(grid), len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '*':
                count += 1
    return count

while m != 0 and n != 0:
    m, n = map(int, input().split())
    mines = []
    if m != 0 and n != 0:
        ans_count += 1
        print(f"Field #{ans_count}:")

    for i in range(m):
        mines.append(list(input()))

    for i in range(m):
        for j in range(n):
            if mines[i][j] == '*':
                temp += '*'
            else:
                temp += str(search(mines, i, j))
        print(temp)
        temp = ""
    print("\n", end = "")