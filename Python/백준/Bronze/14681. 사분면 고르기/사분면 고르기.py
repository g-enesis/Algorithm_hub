def quadrant(x, y):
    if(x > 0):
        # 1,4
        if(y < 0):
            return 4
        if(y > 0):
            return 1
    if(x < 0):
        # 2,3
        if(y < 0):
            return 3 
        if(y > 0):
            return 2
        return


X = int(input())
Y = int(input())

print(quadrant(X, Y))

