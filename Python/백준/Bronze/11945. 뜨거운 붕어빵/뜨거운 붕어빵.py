input_data = input()

a, b = input_data.split(" ")

A, B = int(a), int(b)

for _ in range(A):
    print(input()[::-1])
