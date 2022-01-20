# 1929 소수 구하기

# m, n = map(int, input().split())

# for i in range(m, n+1):
#     if i == 1:
#         continue
#     for j in range(2, int(i ** 0.5)+1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

m, n = map(int, input().split())


def isprime(m, n):
    n += 1
    prime = [True] * n   # 초기화: n개 요소에 True 설정(소수로 간주)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    for i in range(2, int(n**0.5)+1):
        if prime[i]:   # i가 소수인 경우
            for j in range(2*i, n, i):   # i 이후 i의 배수들을 False 판정
                prime[j] = False

    for i in range(m, n):
        if i > 1 and prime[i] == True:
            print(i)


isprime(m, n)
