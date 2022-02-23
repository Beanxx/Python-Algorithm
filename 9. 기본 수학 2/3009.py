# 3009 네 번째 점

x_list = []
y_list = []

for i in range(3):  # 좌표 값 입력 3번 반복
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

# 축에 평행한 직사각형을 만들기 위해서는 네 점의 좌표 중 같은 x, y의 값이 두 개씩 존재해야 함
for i in range(3):
    if x_list.count(x_list[i]) == 1:  # x_list 값들 중 개수가 하나인 값을 x에 넣어줌
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:  # y_list 값들 중 개수가 하나인 값을 y에 넣어줌
        y = y_list[i]

print(x, y)
