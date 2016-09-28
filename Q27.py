#!/usr/bin/python
def is_prime(n):
    return all([(n%j) for j in range(2, int(n**0.5)+1)]) and n>1

list = []
for i in range (2, 1000):
    if is_prime(i):
        list.append(i)

def consecutive(a,b):
    n = 0
    v = b
    while is_prime(v):
        n = n + 1
        v = max(n**2 + n * a + b, 0)
    return n + 1

result = 0
for j in list:
    for k in range (-999,1000):
        if consecutive(k, j) > result:
            result = consecutive(k, j)
            k_final = k
            j_final = j

print (result, k_final, j_final, k_final*j_final)