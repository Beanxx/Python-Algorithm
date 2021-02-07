#1316 그룹 단어 체커

n = int(input())

for i in range(n):
    word = input()
    for j in range(1, len(word)):
        if word.find(word[j-1]) > word.find(word[j]):
            n -= 1
            break
print(n)
