n = int(input())

while n > 0:
    word = input()
    king = word[:2] + '... ' + word + '?'
    print(''.join(king))
    n -= 1
word = []


    """
    A. King's Speech
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
While seeking for a missing item in your backyard, you came into contact with an orb and found yourself at King George VI's court in 1939. He requested you to help him with his stuttering after hearing about your exceptional communication skills. To say a word, the king says the first two letters of the word, pauses, and then says the entire word in question intonation. To assist him in improving his talent, you must first figure out how he would stammer. Determine how he would pronounce a list of words he will use in his speech.

Input
The first line of the input contains a single integer n (1≤n≤105) - the number of words the king will speak

the i-th line of the next n lines contains a word s, (3≤len(s)≤100) - the i-th word the king will speak

Output
For each work the king speaks, output how he would pronounce it.

Example
inputCopy
3
incredible
outstanding
algorithms
outputCopy
in... incredible?
ou... outstanding?
al... algorithms?

    """