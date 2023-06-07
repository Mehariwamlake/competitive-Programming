#!/usr/bin/python3

def solve(n, path1, path2):
    flag = False
    for i in range(n):
        if path1[i] == '1' and path2[i] == '1':
            flag = True
            break
    if flag:
        return "NO"
    else:
        return "YES"



if __name__ == "__main__":
    t = int(input())
    result = []
    for i in range(t):
        n = int(input())
        path1 = input()
        path2 = input()
        result.append(solve(n, path1, path2))
    for x in result:
        print(x)

	 	 	   	 		 		 			    			 		 	