m, n = map(int, input().split())

lista = range(1, 1000000, 2)
listc = [x for x in range(1, len(lista) + 1) if x % 3 != 0]

liste = [x for x in range(1, len(listc) + 1) if x % 7 != 0]

list1 = [i for i in liste if m < i < n]

print(len(list1))
