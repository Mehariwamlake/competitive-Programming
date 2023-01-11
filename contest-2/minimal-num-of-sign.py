n = int(input())

words = [input() for i in range(n)]
out = ['?']*len(word[0])
for word in words:
    for indx, char in enumerate(word):
        if out[indx] =='?' and char != '?':
            out[indx] = char
        elif out[indx] != '?' and char != '?':
            if out[indx] != char:
                out[indx] = '0'

out= ''.join(out)
out =out.replace('?', 'x')
out = out.replace('0', '?')
print(out)

"""
D. Minimal Number of Signs '?'
time limit per test1 s.
memory limit per test256 MB
inputstandard input
outputstandard output
Developers often face with regular expression patterns. A pattern is usually defined as a string consisting of characters and metacharacters that sets the rules for your search. These patterns are most often used to check whether a particular string meets the certain rules.

In this task, a pattern will be a string consisting of small English letters and question marks ('?'). The question mark in the pattern is a metacharacter that denotes an arbitrary small letter of the English alphabet. We will assume that a string matches the pattern if we can transform the string into the pattern by replacing the question marks by the appropriate characters. For example, string aba matches patterns: ???, ??a, a?a, aba.

Programmers that work for the R1 company love puzzling each other (and themselves) with riddles. One of them is as follows: you are given n patterns of the same length, you need to find a pattern that contains as few question marks as possible, and intersects with each of the given patterns. Two patterns intersect if there is a string that matches both the first and the second pattern. Can you solve this riddle?

Input
The first line contains a single integer n (1≤n≤105) — the number of patterns. Next n lines contain the patterns.

It is guaranteed that the patterns can only consist of small English letters and symbols '?'. All patterns are non-empty and have the same length. The total length of all the patterns does not exceed 105 characters.

Output
In a single line print the answer to the problem — the pattern with the minimal number of signs '?', which intersects with each of the given ones. If there are several answers, print any of them.

Examples
inputCopy
2
?ab
??b
outputCopy
xab
inputCopy
2
a
b
outputCopy
?
inputCopy
1
?a?b
outputCopy
cacb
Note
Consider the first example. Pattern xab intersects with each of the given patterns. Pattern ??? also intersects with each of the given patterns, but it contains more question signs, hence it is not an optimal answer. Clearly, xab is the optimal answer, because it doesn't contain any question sign. There are a lot of other optimal answers, for example: aab, bab, cab, dab and so on.
"""

