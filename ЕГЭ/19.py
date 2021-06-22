def f(x, p):
    if x >= 60 and p == 3:
        return True
    elif x >= 60 and p != 3:
        return False
    if p % 2 == 0:
        return f(x * 2, p + 1) \
            or f(x + 3, p + 1)
    else:
        return f(x * 2, p + 1) \
            and f(x + 3, p + 1)


for s in range(2, 57):
    if f(s, 0):
        print(s)
