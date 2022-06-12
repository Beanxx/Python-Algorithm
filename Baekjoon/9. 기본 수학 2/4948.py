# 4948 베르트랑 공준

def sosu(num):
    if num == 1:
        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


# 문제에서 제한한 범위: n <= 123,456 -> 최대를 범위를 2n <= 246,912로 미리 계산
sosu_range = list(range(2, 246912))
sosu_list = []   # 소수담을 빈 리스트

for i in sosu_range:   # 2 <= n <= 246,912
    if sosu(i):   # 소수에 해당하면 소수 리스트에 추가
        sosu_list.append(i)

while(1):
    cnt = 0
    n = int(input())

    if n == 0:   # 0 입력시 입력 종료
        break

    for i in sosu_list:
        if n < i <= 2*n:   # 소수를 담은 리스트가 범위 내에 있으면 카운트
            cnt += 1

    print(cnt)
