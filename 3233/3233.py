"""[LEARNING LOGS] สลากกินแบ่ง"""

x,y = input().split()
x  = x.upper()
a,b = input().split()
a  = a.upper()
z = 0
if y == b:
    z = 100000
elif y[-3:] == b[-3:]:
    z = 200
elif y[-2:] == b[-2:]:
    z = 100
else:
    z = 0

if x == a and z:
    z = z*10
elif x == a and not z:
    z = 20

print(z)
