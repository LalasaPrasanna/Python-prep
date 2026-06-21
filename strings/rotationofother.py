def rotationofother(s,goal):
    if len(s)!= len(goal):
        return False
    newS = s+s
    if goal in newS:
        return True
    return False
s = input()
goal = input()
print(rotationofother(s, goal))
