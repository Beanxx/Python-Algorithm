# 1193 분수찾기

x = int(input())

line = 0  # 해당 줄 번호
end_index = 0  # 해당 line의 마지막 num의 인덱스번호

while end_index < x:
    line += 1
    end_index += line

num = end_index - line  # line=짝수: x와 top의 차, line=홀수: x와 bottom의 차

if line % 2 == 0:  # line이 짝수일 때
    top = x - num
    bottom = line - top + 1
else:  # line이 홀수일 때
    bottom = x - num
    top = line - (bottom) + 1

print(f"{top}/{bottom}")
