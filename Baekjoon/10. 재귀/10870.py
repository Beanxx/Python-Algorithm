# 10872 피보나치 수 5

# 1. for문 사용
n = int(input())

arr = [0, 1]

for i in range(2, n+1):
    num = arr[i-2] + arr[i-1]
    arr.append(num)

print(arr[n])


# 2. 재귀함수 사용
def fibonacci(n):
    if (n > 1):
        return fibonacci(n-2) + fibonacci(n-1)
    else:
        return n


n = int(input())
print(fibonacci(n))
