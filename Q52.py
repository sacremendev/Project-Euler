#!/usr/bin/python
l = 6

def test_nb(i):
    if len(str(i)) == len(set(str(i))):
        sum = 0
        for k in set(str(i)):
            sum += int(k)
            #print(k)
        return sum
    else:
        return 0

#print(test_nb(247194))

#123456,166667

for n in range(123456,166667):
    sum = test_nb(n)
    if sum == 0:
        continue
    else:
        for m in range(2,l+1):
            if test_nb(n*m) == sum:
                if m == l:
                    print(n,m,n*m)
            else:
                break


