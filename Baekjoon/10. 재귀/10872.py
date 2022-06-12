# 10872 팩토리얼

# 1. for문 사용
n = int(input())

result = 1

for i in range(1, n+1):
    result *= i

print(result)


# 2. 재귀함수 사용
def factorial(n):
    if(n > 1):
        return n * factorial(n-1)
    else:
        return 1


n = int(input())
print(factorial(n))

# 3. math library 사용
# import math

# n = int(input())
# print(math.factorial(n))
