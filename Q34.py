#!/usr/bin/python
import math
result = 0
for i in range(3, 2540161):
    sum = 0
    for j in str(i):
        sum += math.factorial(int(j))
    if sum == i:
        #print(i)
        result += i
print(result)