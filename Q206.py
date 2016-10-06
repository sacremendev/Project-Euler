#!/usr/bin/python
#101010101-138902663


def check(i):
    if str(i)[2]!="2":
        return 0
    if str(i)[4]!="3":
        return 0
    if str(i)[6]!="4":
        return 0
    if str(i)[8]!="5":
        return 0
    if str(i)[10]!="6":
        return 0
    if str(i)[12]!="7":
        return 0
    if str(i)[14]!="8":
        return 0
    print(i)
    return 1

for i in range(101010101, 138902663):
    if str(i)[8]=="3" or str(i)[8]=="7":
        sqr=i*i
        if check(sqr)==1:
            print(i)
            break
