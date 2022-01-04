#2292 벌집

n = int(input())

room = 1 # 벌집 개수
plus = 6
count = 1

while n > room:
  room += plus 
  plus += 6 
  count += 1  

print(count)