def is_pangram(n, string):
    string = string.lower()
    letters = set()
    for char in string:
        if char.isalpha():
            letters.add(char)
    if len(letters) == 26:
        return "YES" 
    else:
        return "NO"
n = int(input())
s = input()
print(is_pangram(n,s))