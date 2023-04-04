import sys
import math as m

ls = dict()
for i in range(1, 10000):
    ls[i * i] = i
for line in sys.stdin:
    n = eval(line)
    flag = True
    for a in range(1, int(m.sqrt(n)) + 1):
        for b in range(1, int(m.sqrt(n)) + 1):
            d = a ** 2 + b ** 2
            if n - d in ls and a <= b <= ls[n - d]:
                flag = False
                print("{:d} {:d} {:d}".format(a, b, ls[n - d]))
    if flag:
        print("No Solution")
