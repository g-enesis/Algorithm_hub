
def calc():
    while True:
        A, B = map(int, input().split())
        if A == 0 or B == 0: 
            break
        else:
            print(A + B)

        
calc()