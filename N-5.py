def elem(tpl):
    return all(tpl)
vvod = tuple(map(bool, input().split()))
res = elem(vvod)
print(res)