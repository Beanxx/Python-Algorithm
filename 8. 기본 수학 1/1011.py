# 1011 Fly me to the Alpha Centauri

import sys

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1   # count별 최대 가능 이동 거리
    total = 0  # 이동 거리 합

    while total < distance:
        count += 1
        total += move

        if count % 2 == 0:
            move += 1
    print(count)
