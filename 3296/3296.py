"""1"""

r1,g1,b1 = map(int, input().split())
r2,g2,b2 = map(int, input().split())

x = (r1 + r2) // 2
y = (g1 + g2) // 2
z = (b1 + b2) // 2
x = str(x)
y = str(y)
z = str(z)
A = f"{x} {y} {z}"
print(A)
