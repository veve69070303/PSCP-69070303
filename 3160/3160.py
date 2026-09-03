"""xx"""

x,y = map(int, input().split())

z = []

for i in range(x, y+1):
    if i >= 2:
        count = 0
        for j in range(1, i+1):
            if not i % j:
                count +=1
        if count == 2:
            z.append(i)
if len(z) > 0:
    print(*z)
print(f"Total primes: {len(z)}")
