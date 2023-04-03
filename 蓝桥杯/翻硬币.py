s1 = input()
s2 = input()

start_n = 0
f = 0
summ = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        if f == 0:
            start_n = i
            f = 1
        else:
            summ += i - start_n
            f = 0
print(summ)
