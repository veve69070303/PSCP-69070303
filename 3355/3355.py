"""ko"""
def main():
    """ko"""
    num = []
    while True:
        x = int(input())
        if x == -1:
            break
        num.append(x)

    if not num:
        return

    one = []
    start = num[0]
    end = num[0]

    for i in range(1, len(num)):
        if num[i] == end + 1:
            end = num[i]
        else:
            if start == end:
                one.append(str(start))
            else:
                one.append(f"{start}-{end}")
            start = num[i]
            end = num[i]

    if start == end:
        one.append(str(start))
    else:
        one.append(f"{start}-{end}")

    print(", ".join(one))
main()
