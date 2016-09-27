#!/usr/bin/python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

i = factorial(100)
i_s = str(i)

sum = 0
for n in i_s:
    sum = sum + int(n)
    #print (n)

print (sum)