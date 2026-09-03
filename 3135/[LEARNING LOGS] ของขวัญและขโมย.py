"""[LEARNING LOGS] ของขวัญและขโมย"""

n, k, t = map(int, input().split())
if t == 1:
    print(1)
else:
    kon = 1
    countt = 1
    while True:
        nextt = ((kon - 1 + k) % n) + 1
        if nextt == 1:
            break

        countt += 1

        if nextt == t:
            break

        kon = nextt
    print(countt)
