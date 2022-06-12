#4673 셀프 넘버

# set() : 중복이 없는 요소들로만 구성된 집합 컬렉션 (순서 x)
# 1~10000까지의 숫자 저장
all_num = set(range(1, 10001))

# 셀프 넘버가 아닌 수 저장
not_self_num = set()

for i in range(1, 10001):
    for j in str(i):  # 문자열로 반환하면 예를 들어 123을 1, 2, 3으로 접근 가능
        i += int(j)  # ex) 123 + 1 + 2 + 3 =

    not_self_num.add(i)  # 셀프 넘버가 아닌 수를 계속 저장

# 셀프 넘버 set = 전체 수 set - 셀프 넘버가 아닌 수 set
self_num = sorted(all_num - not_self_num)

for i in self_num:
    print(i)

