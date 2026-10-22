"""sd"""
def main():
    """sd"""
    n = int(input())

    if n <= 1:
        print("NO")
        return

    limit = int(n ** 0.5)

    for i in range(2, limit + 1):
        if not n % i :
            print("NO")
            return

    print("YES")
main()
