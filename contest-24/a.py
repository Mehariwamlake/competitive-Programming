h, w = list(map(int, input().split()))
is_right = True
for i in range(h):
    if i % 2 == 0:
        print("#" * w)
    else:
        cont = "." * (w - 1)
        print(cont + "#" if is_right else "#" + cont)
        is_right = not is_right
