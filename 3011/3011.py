"""[HOMEWORK] Colors"""

color1 = input().capitalize()
color2 = input().capitalize()

a = color1 + color2

if a in "RedRed":
    print("Red")
elif a in "BlueBlue":
    print("Blue")
elif a in "YellowYellow":
    print("Yellow")
elif( a in "RedYellow") or ( a in "YellowRed"):
    print("Orange")
elif ( a in "BlueRed") or ( a in "RedBlue" ):
    print("Violet")
elif ( a in "YellowBlue") or ( a  in "BlueYellow"):
    print("Green")
else:
    print("Error")
