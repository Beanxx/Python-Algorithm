#  1978 소수 찾기

import sys

n = int(input())
num_list = list(map(int, input().split()))

cnt = 0

for i in num_list:
    if i != 1:  # 1은 소수 아님
        for j in range(2, i):  # range: 2 ~ i-1
            if i % j == 0:  # 소수 아닌 경우
                break
        else:  # i가 1과 자신 i를 제외한 어떠한 j로도 나눠지지 않는 경우 = 소수
            cnt += 1
print(cnt)
