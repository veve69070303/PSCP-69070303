"""tem"""

temm = float(input())
one = input()
two = input()

c = temm
c1 = temm + 273.15
c2 = (temm * 9/5) + 32
c3 = (temm + 273.15) * 9/5


ck = temm - 273.15
ckf = (ck * 9/5) + 32
ckr = (ck + 273.15) * 9/5


cf = (temm -32) * 5/9
cfk = cf + 273.15
cfr = (cf + 273.15) * 9/5

cr = (temm * 5/9) - 273.15
crk = cr + 273.15
crf = (cr * 9/5) + 32

if one == "C":
    if two == "C":
        print(f"{c:.2f}")
    elif two == "K":
        print(f"{c1:.2f}")
    elif two == "F":
        print(f"{c2:.2f}")
    elif two == "R":
        print(f"{c3:.2f}")
if one == "K":
    if two == "C":
        print(f"{ck:.2f}")
    elif two == "K":
        print(f"{temm:.2f}")
    elif two == "F":
        print(f"{ckf:.2f}")
    elif two == "R":
        print(f"{ckr:.2f}")
if one == "F":
    if two == "C":
        print(f"{cf:.2f}")
    elif two == "K":
        print(f"{cfk:.2f}")
    elif two == "F":
        print(f"{temm:.2f}")
    elif two == "R":
        print(f"{cfr:.2f}")
if one == "R":
    if two == "C":
        print(f"{cr:.2f}")
    elif two == "K":
        print(f"{crk:.2f}")
    elif two == "F":
        print(f"{crf:.2f}")
    elif two == "R":
        print(f"{temm:.2f}")
