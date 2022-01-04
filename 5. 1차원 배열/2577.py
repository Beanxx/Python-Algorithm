#2577 숫자의 개수

import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
num = str(A * B * C)

for i in range(10):
    print(num.count(str(i)))
