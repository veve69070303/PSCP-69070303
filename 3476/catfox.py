"""[LEARNING LOGS] CuteCat CuteFox"""
import ast

n = int(input())
animals = {}

for _ in range(n):
    line = input().strip()
    d = ast.literal_eval(line)
    animals.update(d)

if "Cat01" not in animals.values() and "Garfield" not in animals:
    animals["Garfield"] = "Cat01"

if "Fox01" not in animals.values() and "Fubuki" not in animals:
    animals["Fubuki"] = "Fox01"

cats = {}
foxes = {}

for name, aid in animals.items():
    if aid.startswith("Cat"):
        cats[name] = aid
    elif aid.startswith("Fox"):
        foxes[name] = aid

sorted_cats = sorted(cats.items(), key=lambda item: int(item[1][3:]))
sorted_foxes = sorted(foxes.items(), key=lambda item: int(item[1][3:]))

print(f"Cat : {len(sorted_cats)}")
print(f"Fox : {len(sorted_foxes)}")

for name, aid in sorted_cats:
    print(f"{name} : {aid}")

for name, aid in sorted_foxes:
    print(f"{name} : {aid}")
