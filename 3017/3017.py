"""Vat"""

sc = int(input())

if sc <= 500:
    TT = 50
elif 500 < sc <= 10000:
    TT = sc * 0.10
else:
    TT = 1000

u = (sc + TT) * 1.07
print(f"{u:.2f}")
