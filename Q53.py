#!/usr/bin/python
import math
def CS(n,r):
    return math.factorial(n)/math.factorial(r)/math.factorial(n-r)

result = 0
for n in range(1,101):
    for r in range(1,int(n/2)+1):
        if CS(n,r)>1000000:
            #print(n,r)
            result += n-r*2+1
            break
print(result)