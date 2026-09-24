"""big"""

line = []
for i in range(5):
    if not i:
        pass
    x = input().strip()
    line.append(x)

y = 0
for j in line:
    if len(j) >= y:
        y = len(j)

bro = "*" * (y + 4)

print(bro)

for o in line:
    dot = " " * (y - len(o))
    print("* " + o + dot + " *")

print(bro)
