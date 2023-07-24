n,k=map(int,input().split())
a=[int(i) for i in input().split()]
count1=0
for i in range(n):
    if(a[i]<=k):
        count1+=1
    else:
        count1+=2
print(count1)
	   	  			 		 		  	 			  	   		