# 1712 손익분기점

A, B, C = map(int, input().split())
n = 0  # 판매량으로써 0으로 초기화 (구하고자 하는 값)

if B >= C:
    print(-1)
else:
    print(int(A/(C-B)+1))
