"""gg"""
def main():
    """gg"""
    x = int(input())
    z =[]
    aim = 0
    for _ in range(x):
        o = int(input())
        z.append(o)

    if x == 1:
        aim = 1
    else:
        for i in range(x):
            if not i:
                if z[0] > z[1]:
                    aim += 1
            elif i == x - 1:
                if z[i] > z[i-1]:
                    aim += 1
            else:
                if z[i] > z[i-1] and z[i] > z[i + 1]:
                    aim += 1

    print(aim)
main()
