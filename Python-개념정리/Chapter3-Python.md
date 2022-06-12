# 📘 '파이썬 알고리즘 인터뷰' 책을 읽고 파이썬 개념을 정리합니다.

## 3장. 파이썬

### ☑️ Naming Convention

- snake case(\_): 변수명, 함수명(소문자)

### ☑️ Type Hint

```python
# 'Type Hint' example
def fn(a:int) -> bool:
```

### ☑️ List Comprehension

: 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문

```python
[n * 2 for n in rnage(1, 10+1) if n % 2 == 1]

# [2, 6, 10, 14, 18]
```

✋ cf. Dictionary Comprehension

```python
a = {key: value for key, value in original.items()}
```

### ☑️ Generator

: 루프의 반복 동작을 제어할 수 있는 루틴 형태

- `yield`: Generator가 여기까지 실행 중이던 값을 내보낸다. <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  중간 값을 리턴한 다음 함수 종료 X 계속 맨 끝 도달까지 실행

```python
# 'yield' example
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n
```

- `next()`: 다음 값 추출

### ☑️ range

: for문에서 사용시 next()를 호출하듯 매번 다음 숫자를 생성

```python
# 'for' example
for i in range(5):
    print(i, end=' ')

# 0 1 2 3 4
```

### ☑️ enumerate

: list()로 결과 추출. index 자동부여

```python
# 'for' example
for i, v in enumerate(a):
    print(i, v)

# 0 1 2 3 4
```

### ☑️ // 나눗셈 연산자

: 몫 return

```
5 / 3 => 1.666...
5 // 3 => 1 (몫)
5 % 3  => 2 (나머지)
```

✋ cf. 몫 & 나머지를 한번에 구할 때

```
divmod(5, 3)
=> (1, 2)
```

### ☑️ print

```python
# 1
print('A1', 'A2')
=> A1 B2

# 2
print('A1', 'B2', sep=",')
=> A1, B2

# 3
print('aa', end=' ') # 줄바꿈 X
print('bb')
=> aa bb
```

- `join()`: 리스트 출력

```python
a = ['A', 'B']
print(' '.join(a))

# A B
```

- format()

```python
print('{0}: {1}'.format(idx+1, fruit))

# 2: Apple
```

- f-string

```python
print(f'{idx+1}: {fruit}')

# 2: Apple
```

### ☑️ Pass

: Null 연산으로 아무것도 하지 않는 기능 => 오류 방지 역할

### ☑️ locals

: Local Symbol Table Dictionary를 가져오는 메소드
