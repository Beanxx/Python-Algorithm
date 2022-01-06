# 2869 달팽이는 올라가고 싶다
import sys
import math

a, b, v = map(int, input().split())

day = 0

day = (v-b) / (a-b)

print(math.ceil(day))
