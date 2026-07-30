"""Season"""

Season = int(input())
Day = int(input())

if  1 <= Season <= 2:
    print ("winter")
elif Season == 3 and Day < 21:
    print ("winter")
elif Season == 3 and Day >= 21:
    print ("spring")
elif 4 <= Season <= 5:
    print ("spring")
elif Season == 6 and Day < 21:
    print ("spring")
elif Season == 6 and Day >= 21:
    print ("summer")
elif 7 <= Season <= 8:
    print ("summer")
elif Season == 9 and Day < 21:
    print ("summer")
elif Season == 9 and Day >= 21:
    print ("fall")
elif 10 <= Season <= 11:
    print ("fall")
elif Season == 12 and Day < 21:
    print ("fall")
elif Season == 12 and Day >= 21:
    print ("winter")
