#!/usr/bin/python
def count(n):
    k = 0
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        k = k + 1
        #print n
    #print k
    return k

result = 0
for i in range(1, 1000000):
    num = count(i)
    if num > result:
        print ("update ", i, " ", num)
        result = num
print (result)
