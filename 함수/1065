#1065 한수

N = int(input())
hansu = 0

for i in range(1, N+1):
    if i <= 99: #100 미만의 수는 하나 또는 두 수만 비교하므로 모든 수가 등차수열 즉, 한수가 될 수 있다.
        hansu += 1

    else:
        num = list(map(int, str(i)))  #ex) 123 -> [1, 2, 3]
        if num[0] - num[1] == num[1] - num[2]:
            hansu += 1
print(hansu)
