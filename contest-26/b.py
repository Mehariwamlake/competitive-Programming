for _ in range(int(input())):
    n = int (input())
    list1 =[int(i) for i in input().split()]
    list1.sort()
    sum1 = sum(list1[:(n-1)//2 + 1])
    sum2 = sum(list1[n//2 + 1:])
    if sum2 > sum1:
        print ("YES")
    else: 
        print("NO")  			 		  	   				  			