"""y"""
def main():
    """y"""
    n, p = map(int, input().split())
    cool = []
    for _ in range(n):
        row = input().split()
        row = list(map(int, row))
        cool.append(row)

    col_count = [0] * n
    col_sum = [0] * n
    total_tiles = 0
    total_points = 0

    for i in range(n):
        row_tiles = 0
        row_points = 0
        for j in range(n):
            val = cool[i][j]
            row_points += val
            col_sum[j] += val
            if val > 0:
                row_tiles += 1
                col_count[j] += 1
        total_tiles += row_tiles
        total_points += row_points
        print(*cool[i], row_tiles, row_points)
    print(*col_count)
    print(*col_sum)
    print(f"{total_tiles} {total_points} {total_points * p:.2f}")
main()
