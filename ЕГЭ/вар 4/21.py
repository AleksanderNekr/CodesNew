def f(n, k, p):
    if n >= 0 and k >= 0:
        if (n == 0 or k == 0 or (n == 1 or n == 3) and (k == 1 or k == 3)) and (p == 2 or p == 4):
            return True
        elif (n == 0 or k == 0 or (n == 1 or n == 3) and (k == 1 or k == 3)) and p != 2 and p != 4:
            return False
        if p % 2 > 0:
            if n % 2 == 0 and k % 2 == 0:
                return f(n - 4, k - 4, p + 1) or f(n / 2, n / 2, p + 1) or f(k / 2, k / 2, p + 1)
            elif n % 2 == 0:
                return f(n - 4, k - 4, p + 1) or f(n / 2, n / 2, p + 1)
            elif k % 2 == 0:
                return f(n - 4, k - 4, p + 1) or f(k / 2, k / 2, p + 1)
            else:
                return f(n - 4, k - 4, p + 1)
        else:
            if n % 2 == 0 and k % 2 == 0:
                return f(n - 4, k - 4, p + 1) and f(n / 2, n / 2, p + 1) and f(k / 2, k / 2, p + 1)
            elif n % 2 == 0:
                return f(n - 4, k - 4, p + 1) and f(n / 2, n / 2, p + 1)
            elif k % 2 == 0:
                return f(n - 4, k - 4, p + 1) and f(k / 2, k / 2, p + 1)
            else:
                return f(n - 4, k - 4, p + 1)


for k in range(1, 100):
    if f(30, k, 0):
        print(k)
