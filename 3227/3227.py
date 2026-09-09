"""[LEARNING LOGS] ไพ่ 44 ใบ"""

x = input().upper()
if len(x) == 2:
    if x[1] == "D":
        if x[0] == "A":
            print("ace of diamonds")
        elif x[0] == "J":
            print("jack of diamonds")
        elif x[0] == "Q":
            print("queen of diamonds")
        elif x[0] == "K":
            print("king of diamonds")
        elif x[0] == "2":
            print("2 of diamonds")
        elif x[0] == "3":
            print("3 of diamonds")
        elif x[0] == "4":
            print("4 of diamonds")
        elif x[0] == "5":
            print("5 of diamonds")
        elif x[0] == "6":
            print("6 of diamonds")
        elif x[0] == "7":
            print("7 of diamonds")
        elif x[0] == "8":
            print("8 of diamonds")
        elif x[0] == "9":
            print("9 of diamonds")
    if x[1] == "H":
        if x[0] == "A":
            print("ace of hearts")
        elif x[0] == "J":
            print("jack of hearts")
        elif x[0] == "Q":
            print("queen of hearts")
        elif x[0] == "K":
            print("king of hearts")
        elif x[0] == "2":
            print("2 of hearts")
        elif x[0] == "3":
            print("3 of hearts")
        elif x[0] == "4":
            print("4 of hearts")
        elif x[0] == "5":
            print("5 of hearts")
        elif x[0] == "6":
            print("6 of hearts")
        elif x[0] == "7":
            print("7 of hearts")
        elif x[0] == "8":
            print("8 of hearts")
        elif x[0] == "9":
            print("9 of hearts")
    if x[1] == "S":
        if x[0] == "A":
            print("ace of spades")
        elif x[0] == "J":
            print("jack of spades")
        elif x[0] == "Q":
            print("queen of spades")
        elif x[0] == "K":
            print("king of spades")
        elif x[0] == "2":
            print("2 of spades")
        elif x[0] == "3":
            print("3 of spades")
        elif x[0] == "4":
            print("4 of spades")
        elif x[0] == "5":
            print("5 of spades")
        elif x[0] == "6":
            print("6 of spades")
        elif x[0] == "7":
            print("7 of spades")
        elif x[0] == "8":
            print("8 of spades")
        elif x[0] == "9":
            print("9 of spades")
    if x[1] == "C":
        if x[0] == "A":
            print("ace of clubs")
        elif x[0] == "J":
            print("jack of clubs")
        elif x[0] == "Q":
            print("queen of clubs")
        elif x[0] == "K":
            print("king of clubs")
        elif x[0] == "2":
            print("2 of clubs")
        elif x[0] == "3":
            print("3 of clubs")
        elif x[0] == "4":
            print("4 of clubs")
        elif x[0] == "5":
            print("5 of clubs")
        elif x[0] == "6":
            print("6 of clubs")
        elif x[0] == "7":
            print("7 of clubs")
        elif x[0] == "8":
            print("8 of clubs")
        elif x[0] == "9":
            print("9 of clubs")
if len(x) == 3:
    if x[0] == "1" and x[1] == "0":
        if x[2] == "D":
            print("10 of diamonds")
        elif x[2] == "H":
            print("10 of hearts")
        elif x[2] == "S":
            print("10 of spades")
        elif x[2] == "C":
            print("10 of clubs")
