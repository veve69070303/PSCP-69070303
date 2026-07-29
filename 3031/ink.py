"""ink"""
import math as i
S,N = map(int, input().split())
PI = 3.1416
for _ in range(N):
    if not _:
        pass
    X,Y = map(int, input().split())
    r = i.sqrt(X**2 + Y**2)
    alll = PI * (r**2)
    kon = i.ceil(alll / S)
    print(kon)
