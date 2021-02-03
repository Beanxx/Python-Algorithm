#1157 단어 공부

a = input().upper()  # 대문자로 변경
lists = list(set(a))  # 중복된 문자를 정렬
c = []

for i in lists:
    counts = a.count(i)  # 입력한 알파벳의 개수를 count
    c.append(counts)

if c.count(max(c)) >= 2:  # 리스트 중 많이 나온 문자가 2개 이상일 경우
    print("?")
else:
    print(lists[(c.index(max(c)))])
