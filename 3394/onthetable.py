"""ontheteble"""
def main():
    """onthetable"""
    n, s = map(int, input().split())
    forward = [0] * (n + 1)
    for i in range(1,n+1):
        forward[i] = int(input())

    visit = set()
    cerrent = s
    while cerrent and cerrent not in visit:
        visit.add(cerrent)
        cerrent = forward[cerrent]

    print(len(visit))
main()
