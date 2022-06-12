# 9020 골드바흐의 추측

import sys


def sosu(num):
    for i in range(2, int(pow(num, 0.5)) + 1):  # pow(num, 0.5) = num**0.5
        if num % i == 0:  # 소수가 아닌 경우
            return False
    if num == 1:  # 1은 항상 소수가 아님
        return False
    return True  # 위의 경우 외에는 소수라고 판단


T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    for num in range(n // 2, 0, -1):  # n//2 ~ 0 까지, -1씩 작아지도록
        if sosu(num) and sosu(n-num):
            print(num, n-num)
            break
