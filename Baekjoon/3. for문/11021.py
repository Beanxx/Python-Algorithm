#11021 A+B - 7

T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    print("Case #%s : %s" % (i, a+b))
