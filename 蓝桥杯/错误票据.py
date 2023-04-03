n = int(input())

lista = []

for i in range(n):
    a = list(map(int, input().split()))
    for j in a:
        lista.append(j)
lista.sort()
for i in range(1, len(lista)):
    if lista[i] == lista[i-1]+1:
        continue
    if lista[i] != lista[i-1]:
        print(lista[i] - 1, end=' ')
listb = list(set([x for x in lista if lista.count(x) > 1]))
print(listb[0])

