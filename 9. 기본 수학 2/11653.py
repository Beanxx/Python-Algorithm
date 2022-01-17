# 11653 소인수분해

n = int(input())

while n != 1:  # n이 1이 될 때 까지 반복
    for i in range(2, n+1):  # 범위: 2 ~ n
        if(n % i == 0):  # n을 2부터 순차적으로 나누기
            print(i)  # n이 나머지 없이 나눠지면 출력
            n = n // i
            break
