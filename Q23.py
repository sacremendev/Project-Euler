#!/usr/bin/python
def factors(n):
	sum = 0
	for i in range(1,int((n)/2)+1):		
		if (n % i) == 0:
			sum = sum + i
	#print (sum)
	return sum

def is_abundant(n):
    if factors(n) > n:
        return 1
        
def is_sum_abundant(n):
    for i in range(1, int(n/2) + 1):
        if is_abundant(i) and is_abundant(n-i):
            #print (n, "is the sum of two abundant numbers")
            return 1
            break
        
result = 0
for k in range(1, 25):
    if is_sum_abundant(k) != 1:
        result = result + k
print (result)

#21740