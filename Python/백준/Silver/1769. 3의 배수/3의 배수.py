
def schedules(x):
    count = 0
    while len(x) > 1:
        count += 1
        x = str(sum(map(int, x)))

    if int(x) in [3,6,9]:
        result = "YES"
    else:
        result = "NO"

    return count, result


x = input().strip()
count, result = schedules(x)
print(count)
print(result)