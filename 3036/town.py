"""ppy"""

lof = int(input())
floor = 1
while floor ** 2 < lof:
    floor += 1
far = (floor ** 2) - lof
ROOM = (2*(floor)) - 1
if not far % 2:
    print(ROOM - 1)
else:
    print(ROOM - 2)
