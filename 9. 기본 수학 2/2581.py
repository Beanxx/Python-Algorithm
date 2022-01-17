# 2581 소수

m = int(input())
n = int(input())

arr = []  # 빈 배열

for i in range(m, n+1):  # range: m ~ n
    if i == 1:  # 1은 소수 아님
        pass
    elif i == 2:  # 2는 소수임
        arr.append(i)
    else:
        for j in range(2, i):  # range: 2 ~ i-1
            if i % j == 0:  # 무언가로 나눠지는 i는 소수가 아님
                break
            elif j == i-1:  # j가 범위 끝인 i-1까지 도달했다면
                arr.append(i)  # i를 소수 배열에 추가

if len(arr) == 0:
    print('-1')
else:
    print(sum(arr))
    print(min(arr))
