a = input()
b = input()


result = []
for i, j in zip(a,b):
    if(i == j):
        if i == 0:
            result.append('1')
        else:
            result.append('0')
    else:
        result.append('1')

print("".join(result))
 	  	  	 	 	   	 		   	  		  		