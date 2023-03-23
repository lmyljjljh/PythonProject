import random

# for k in range(100):
n = int(input())
# n3 = random.randint(1, 5)
a = list(map(int, input().split()))
# a = []
# for i in range(n3):
#     n1 = random.randint(1, 11)
#     n2 = random.randint(1, 1000)
#     for i in range(n1):
#         a.append(n2)
#         n2 += 1
# print(a)
lenn = 1
lenx = 1
summ = a[0]
# n = len(a)
# s1 = str(n) + '\n'
# for i in range(n):
#     if i < n - 1:
#         s1 += str(a[i]) + ' '
#     else:
#         s1 += str(a[i])
# with open(r'.\1\{}.in'.format(k), 'w') as fp:
#     fp.write(s1)
for i in range(1, n):
    if a[i] == a[i - 1] + 1:
        lenn += 1
        if i == n - 1:
            if lenn >= lenx:
                lenx = lenn
                summ = a[i - lenn + 1]
    else:
        if lenn >= lenx:
            lenx = lenn
            summ = a[i - lenn]
        lenn = 1
print(summ)
# with open(r'.\1\{}.out'.format(k), 'w') as fp:
#     fp.write(str(summ))
