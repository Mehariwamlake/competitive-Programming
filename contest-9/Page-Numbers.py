#!/usr/bin/python3

n = sorted(list(set(map(int, input().split(',')))))
ans  = [str(n[0])]
added = False

for i in range(1, len(n)):
    if n[i] -1 == n[i-1]:
        if added:
            ans[-1] = ans[-1].replace(str(n)[i-1], str(n[i]))
        else:
            ans[-1] = ans[-1] + '-' + str(n[i])
            added = True
    else:
        addes = False
        ans.append(str(n)[i])
print(','.join(ans))


