def pal(inp):
    chist = ''.join(char.lower() for char in inp if char.isalnum())
    return chist == chist[::-1]

wht = input()
if pal(wht):
    print("palind")
else:
    print("not palind")
