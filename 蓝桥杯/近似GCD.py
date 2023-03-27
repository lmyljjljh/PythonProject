def gongyueshu(x, y):
    a, b = x, y
    while b:
        a, b = b, a % b
    return a


n, g = map(int, input().split())

nums = list(map(int, input().split()))

res = 0

x = 0

while x < len(nums) - 1:
    j = x + 1
    key = 1
    if nums[x] < g and nums[j] < g:
        continue
    if gongyueshu(nums[x], nums[j]) == g:
        z = j + 1
        while z < len(nums) and nums[z] % g == 0:
            z += 1
        res += z - x
        x += 1
    else:
        if nums[x] % g == 0 or nums[j] % g == 0:
            z = x + 2
            while z < len(nums) and nums[z] % g == 0:
                z += 1
            z -= 1
            res += z - x
            x += 1
        else:
            x += 1
print(res)
