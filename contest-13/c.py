n = int(input()) 
count = 0
while n > 9:
	sum = 0
	for i in str(n):
		sum += int(i)
	n = sum
	count += 1
print(count) 