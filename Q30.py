#!/usr/bin/python
result = 0
for i in range(2, 354295):
    i_s = str(i)
    mul = sum([(int(i_s[j])**5) for j in range(len(i_s))])
    if mul == i:
        print (mul)
        result = result + mul

print (result)
