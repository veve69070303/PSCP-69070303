"""new"""
def main():
    """new"""
    x = {"Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts",
    "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts"}
    y = {"Sweet", "Sour", "Salty"}

    a = set()
    while True:
        agv = input()
        if agv == "Cook":
            break
        a.add(agv)
    b = set()
    while True:
        brk = input()
        if brk == "End":
            break
        b.add(brk)
    cambodog = not a.issubset(x)
    bangkok = x == a
    singapore = y == b

    if bangkok and singapore:
        print("Delicious!")
    elif bangkok and not singapore:
        print("Not Bad...")
    elif cambodog:
        print("This is not Pad Thai!!!")
    elif not bangkok:
        print("This is bad!")
main()
