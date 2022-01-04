#10809 알파벳 찾기

S = input()

for i in range(97, 123):  # ASCII CODE로 소문자 a~z = 97~122 의미
    print(S.find(chr(i)), end=' ')  
    # find() : 특정 문자를 찾고 위치 반환(뒤에 명시하지 않을 경우 index 0부터 시작), 찾는 문자가 없을경우 -1 return
