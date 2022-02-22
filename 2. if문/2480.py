# 2480 주사위 세개

one, two, three = map(int, input().split())

if one == two and two == three:
    print(10000 + (one * 1000))
elif one == two or one == three or two == three:
    if one == two or one == three:
        print(1000 + (one * 100))
    else:
        print(1000 + (three * 100))
elif one != two and two != three:
    print(max(one, two, three) * 100)
