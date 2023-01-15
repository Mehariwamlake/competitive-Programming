while True:
    n = int(input())
    if n in range(1,101):
        break
word_list = []
for i in range(n):
    while True:
        word = input()
        if len(word) in range(1,101):
            break
    word_list.append(word.lower())

for _ in word_list:
    if len(_) > 10:
        print(_[0] + str(len(_[1:-1])) + _[-1])
    else:
        print(_)