#8958 OX퀴즈

N = int(input())

for i in range(N):
    ox = input()
    ox_list = list(ox)
    score = 0
    result = 0

    for j in range(len(ox)):
        if ox_list[j] == 'O':
            score += 1
            result += score

        elif ox_list[j] == 'X':
            score = 0

    print(result)
