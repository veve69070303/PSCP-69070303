"""SurprisingVote"""

alll = float(input())
maxalll = float(input())

minall = alll - maxalll - maxalll

if minall < 0:
    minall = 0
if maxalll - minall >2:
    print("Surprising")
else:
    print("Not surprising")
