def f(x, y, p):
    if (x <= 1 or y <= 1) and p == 2:
        return True
    elif x > 1 and y > 1 and p == 2 or x <= 1 or y <= 1:
        return False
    if x % 2 == 0 and y % 2 == 0:
        return f(x - 3, y - 3, p + 1) or f(x / 2, x / 2, p + 1) or f(y / 2, y / 2, p + 1)
    elif x % 2 == 0:
        return f(x - 3, y - 3, p + 1) or f(x / 2, x / 2, p + 1)
    elif y % 2 == 0:
        return f(x - 3, y - 3, p + 1) or f(y / 2, y / 2, p + 1)
    else:
        return f(x - 3, y - 3, p + 1)


for s in range(1, 1000):
    if f(32, s, 0):
        print(s)
