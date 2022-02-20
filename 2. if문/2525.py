# 2525 오븐 시계

h, m = map(int, input().split())
time = int(input())

h += time // 60  # 몫
m += time % 60   # 나머지

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

print(h, m)