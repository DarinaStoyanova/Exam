

N = int(input())
M = int(input())
S = int(input())

for number in range (M, N - 1, -1):
    if number % 2 == 0 and number % 3 == 0:
        if number == S:
            break
        print (f"{number}",end=" ")