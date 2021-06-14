def f(x, y, p):
    if x+y >= 77 and p == 3:
        return True
    elif x+y < 77 and p == 3:
        return False
    elif x+y >= 77:
        return False
    if p % 2 != 0:
        return f(x+1, y, p+1) and f(x+y*2, y, p+1) and f(x, y+1, p+1) and f(x, y+x*2, p+1)
    else:
        return f(x+1, y, p+1) or f(x+y*2, y, p+1) or f(x, y+1, p+1) or f(x, y+x*2, p+1)


for s in range(1, 68):
    if f(9, s, 0):
        print(s)
