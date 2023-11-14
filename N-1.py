def lst(num):
    res = 1
    for num in num:
        res *= num
    return res

num = [int(x) for x in input().split()]
res = lst(num)
print(res)
