someVar = 1
#someVar is global
print(someVar)

def someFunc():
    someVar = 2
#someVar is limited within function
    return someVar

print(someFunc())
