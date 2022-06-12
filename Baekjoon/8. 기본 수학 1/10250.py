# 10270 ACM 호텔

import sys

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n // h + 1  # 몫
    floor = n % h  # 나머지

    if n % h == 0:
        num = n // h
        floor = h

    print(f'{floor*100+num}')
