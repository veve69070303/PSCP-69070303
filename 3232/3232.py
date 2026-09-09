"""flog"""

x,y = map(int, input().split())

a = 0
b = 0
for i in range(y):
    a += x - (2 * i)
    b += 1
    if a >= y:
        break

if a < y:
    print(-1)
else:
    print(b)
