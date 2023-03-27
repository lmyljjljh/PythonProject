T = int(input())
while T:
    T -= 1
    n, m = map(int, input().split())

    f = 0
    for i in range(1, m+1):
        if f:
            break
        for j in range(1, i):
            if n % i == n % j:
                f = 1
                break
    if f:
        print("Yes")
    else:
        print("No")
