test = int(input())
for i in range(test):
    num = int(input())
    a = -1
    lista = list(map(int,input().split()))
    for j in range(num):
        if lista[j] % 2 != 0:
            a = 0
            print(lista[j])
            break
    if a != 0:
        print(lista[0])
  				  	 		   		 	 	 	 	  	 		