#!/usr/bin/python

i = pow(2, 1000)
i_s = str(i)

sum = 0
for n in i_s:
    sum = sum + int(n)
    #print (n)

print (sum)