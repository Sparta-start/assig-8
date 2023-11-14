def cnt(inp):
    up = sum(1 for char in inp if char.isupper())
    low = sum(1 for char in inp if char.islower())
    return up, low

wht = input()
upper, lower = cnt(wht)
print(upper)
print(lower)
