"""nok"""
def main():
    """nok"""
    x = int(input())
    y = int(input())
    o = x + y
    a = []
    q = []
    r = 0
    for i in range(o):
        num = int(input())
        a.append(num)

    b = a[x:]
    c = a[:x]

    for i in c:
        for p in b:
            if i == p:
                q.append(i)
                r += 1

    q.sort()
    q.reverse()
    if not r:
        print("Nope")
    else:
        for i in q:
            print(i)

main()
