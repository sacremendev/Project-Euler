#!/usr/bin/python
from numpy import vdot
money = [200, 100, 50, 20, 10, 5, 2, 1]
count = 0
for a in range(2):
    for b in range(3):
        if vdot([a, b, 0, 0, 0, 0, 0, 0], money) > 200:
            break
        for c in range(5):
            if vdot([a, b, c, 0, 0, 0, 0, 0], money) > 200:
                break
            for d in range(11):
                if vdot([a, b, c, d, 0, 0, 0, 0], money) > 200:
                    break
                for e in range(21):
                    if vdot([a, b, c, d, e, 0, 0, 0], money) > 200:
                        break
                    for f in range(41):
                        if vdot([a, b, c, d, e, f, 0, 0], money) > 200:
                            break
                        for g in range(101):
                            if vdot([a, b, c, d, e, f, g, 0], money) > 200:
                                break
                            for h in range(201):
                                if vdot([a, b, c, d, e, f, g, h], money) == 200:
                                    count = count + 1
                                    print(a, b, c, d, e, f, g, h)
                                    break
print (count)
