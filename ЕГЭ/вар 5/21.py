def f(x, y, p):
    if x + y >= 808 and (p == 2 or p == 4):
        return True
    elif x + y < 808 and p == 4 or x + y >= 808:
        return False
    if p % 2 == 0:
        return f(x + 2, y, p + 1) and f(x, y + 2, p + 1) and f(x * 3, y, p + 1) and f(x, y * 3, p + 1)
    else:
        return f(x + 2, y, p + 1) or f(x, y + 2, p + 1) or f(x * 3, y, p + 1) or f(x, y * 3, p + 1)


for s in range(1, 301):
    if f(35, s, 0):
        print(s)
        break
