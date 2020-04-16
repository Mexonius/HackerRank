# https://www.hackerrank.com/challenges/nested-list/problem

# for _ in range(int(input())):
#     name = input()
#     score = float(input())
phy_class = [ [input(), float(input())] for _ in range(int(input()))]

many = len(phy_class)
if 2<=many<=5:
    scores=[ s for [n,s] in phy_class ]
    # find the lowest
    minscore=min(scores)
    # remove every instance from my score's list
    while(scores.count(minscore)):
        scores.remove(minscore)
    # found the second
    second_lowest = min(scores)
    # retrieve the student(s) with that score
    names = sorted(
        [ phy_class[e][0] for e in range(many) if phy_class[e][1]==second_lowest] )
    for _ in names:
        print(_)   
