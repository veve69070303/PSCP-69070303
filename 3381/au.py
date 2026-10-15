"""au"""
def main():
    """au"""
    x = int(input())

    for _ in range(x):
        y = int(input())
        bro = []
        for _ in range(y):
            a, b = map(int, input().split())
            bro.append([a + b, -b, a, b])

        bro.sort()
        for p in bro:
            print(f"{p[2]} {p[3]}")
main()
