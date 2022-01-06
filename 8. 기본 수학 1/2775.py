# 2775 부녀회장이 될테아

import sys

t = int(input())

for i in range(t):
    k = int(input())  # 층
    n = int(input())  # 호

    base = [i for i in range(1, n+1)]  # 0층에 대한 호

    for j in range(k):
        for i in range(1, n):
            base[i] += base[i-1]
    print(base[-1])
