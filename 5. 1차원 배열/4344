#4344 평균은 넘겠지

C = int(input())

for i in range(C):

    inputs = list(map(int, input().split()))
    num = int(inputs[0])
    del inputs[0]
    inputs_sum = int(sum(inputs))
    mean = inputs_sum / num
    person = 0
    result = 0

    for j in range(num):
        if inputs[j] > mean:
            person += 1

    result = (person/num) * 100
    final = format(result, ".3f")
    print(final + "%")
