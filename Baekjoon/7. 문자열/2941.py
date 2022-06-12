#2941 크로아티아 알파벳

words = input()
s = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in s:
    words = words.replace(i, 's')
print(len(words))
