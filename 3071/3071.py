"""A,B"""

A = int(input())
B = int(input())
d = int(input())
r = int(input())
io = 0
for i in range(A,B+1):
    if i % d == r:
        io += 1
print(io)
