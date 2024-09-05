def test(year):
    # 4의 배수이면서 100의 배수가 아닐 때 또는 400의 배수일 때
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return 1
    return 0



year = int(input())
print(test(year))