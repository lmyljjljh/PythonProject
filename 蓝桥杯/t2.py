# summ = 0
# for i in range(30, 100):
#     song = i - 27
#     x = str(i)
#     y = int(x[1]+x[0])
#     if song == y:
#         summ+=1
# print(summ)

# f = 0
# x = 0
# for i in range(100):
#     summ = 0
#     if f:
#         break
#     for j in range(i, 100):
#         summ += j
#         if summ == 236:
#             x = i
#             f = 1
#             break
# print(x)

summ = 0
x = [[-1, 10, 10, 10, -1], [10, 10, 10, 10, -1], [10, 10, 10, -1, -1]]


def f1(n,x):
    global summ
    if n == 9:
        summ += 1
    for i in range(3):
        for j in range(4):
            if x[i][j] == 10:
                if i == 0:
                    if (x[i+1][j-1] != n-1) and (x[i+1][j] != n-1) and (x[i+1][j+1] != n-1) and (x[i][j+1] != n-1):
                        x[i][j] = n
                        f1(n+1, x)
                        x[i][j] = 10
                if i == 1:
                    if j == 0:
                        if (x[i+1][j] != n - 1) and (x[i + 1][j+1] != n - 1) and (x[i][j + 1] != n - 1):
                            x[i][j] = n
                            f1(n + 1, x)
                            x[i][j] = 10
                    else:
                        if (x[i+1][j] != n - 1) and (x[i + 1][j+1] != n - 1) and (x[i][j + 1] != n - 1) and (x[i+1][j-1] != n-1) and (x[i][j-1] != n-1) and (x[i-1][j] != n-1):
                            pass


