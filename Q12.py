#!/usr/bin/python
def factors(n):
	count=0
	for i in range(1,int((n)/2)+1):		
		if (n % i) == 0:
			count = count + 1
	#print ((n) , " ", (count+1))
	return count+1
		
a = 1
c = 0
result=1

while result < 500:
	c = c + a
	a = a + 1
	result = factors(c)
	
print ((c) , " ", (result))
