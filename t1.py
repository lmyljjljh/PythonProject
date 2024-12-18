import random
# for i in range(100):
n, m = map(int, input().split())
# n = random.randint(1, 10000)
# print(n, end=' ')
# m = random.randint(0, n)
# print(m)
lista = []
s2 = str(n)+' '+ str(m)+'\n'
for j in range(n):
    s1, x = map(str, input().split())
    # s1 = ''
    # base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    # length = len(base_str) - 1
    # randomlength = random.randint(1, 20)
    # for k in range(randomlength):
    #     s1 += base_str[random.randint(0, length)]
    # x = random.randint(0, 10000)
    dita = {'name': s1, 'count': int(x)}
    lista.append(dita)
#     if j < n - 1:
#         s2 += s1 + ' ' + str(x) + '\n'
#     else:
#         s2 += s1 + ' ' + str(x)
# with open(r'.\1\{}.in'.format(i+1), 'w') as fp:
#     fp.write(s2)
ditb = sorted(lista, key=lambda x: (-x['count'], x['name']))
s3 = ''
for j in range(m):
    print(ditb[j]['name'], end=' ')
    print(ditb[j]['count'])
#     if j < m - 1:
#         s3 += ditb[j]['name'] + ' ' + str(ditb[j]['count']) + '\n'
#     else:
#         s3 += ditb[j]['name'] + ' ' + str(ditb[j]['count'])
# with open(r'.\1\{}.out'.format(i+1), 'w') as fp:
#     fp.write(s3)

print 1
print 2
