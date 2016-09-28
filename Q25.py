#!/usr/bin/python
def nb_digit(n):
    n_s = str(n)
    return len(n_s)

a = 1
b = 1
n = 2
result = 0
while result < 1000:
    c = a + b
    a = b
    b = c
    n = n + 1
    result = nb_digit(c)
print (n)