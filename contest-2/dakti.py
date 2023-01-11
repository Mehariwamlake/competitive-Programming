import re
n= int(input)
output = []

for i in range(n):
    dic = {}
    listt = []
    string = input()
    words = string.split()
    
    numbers = re.findall(r"\d+", string)
    numbers = [int(s) for s in numbers]
    dic ={k: v for k, v in zip(numbers, words)}
    sorted_dic = dict(sorted(dic.items(), key=lambda item: item[0]))

    for key, value in sorted_dic.items():
        listt.append(value.replace(str(key), ''))
    output.append(' '.join(listt))

for st in output:
    print(st)






"""
C. Dakti
time limit per test1 s.
memory limit per test256 MB
inputstandard input
outputstandard output
Juan loves the Dakti song and wants to memorize the chorus of the song. His friend sent him the chorus in phrases, but the phrases are somewhat strange; they do not have an order and they have numbers. His friend helps Juan organize the chorus of the song.

First, sort the words based on the numbers they have inside them, then delete the numbers once they are organized. i.e A word that has "1" in it comes first, "2" comes second and so on.

Input
The first line contains a single integer t (1≤t≤2∗104) - the number of test cases.

the i-th line of the next t lines contain a single string s (3≤len(s)≤200) - the chorus of the song.

Output
For each test case output the words of the chorus organized based on the numbers and the numbers removed.

Example
inputCopy
3
worl2d hell1o
i2s th1s a3 t4est
yo2u cr3azy? a1re
outputCopy
hello world
ths is a test
are you crazy?
Note
In the first example "hello" comes before "world" since it has the digit 1 in it whereas world has 2.
"""