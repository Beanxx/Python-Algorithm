#1110 더하기 사이클

N = num = int(input())
cycle = 0

while True:
    ten = N // 10
    one = N % 10
    total = ten + one
    cycle += 1
    N = int(str(one) + str(total % 10))

    if (num == N):
        break

print(cycle)
