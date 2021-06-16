def f(N, K, p):
    if N >= 0 and K >= 0:
        if (N == 0 or K == 0 or (N == 1 or N == 3) and (K == 1 or K == 3)) and p == 3:
            return True
        elif (N == 0 or K == 0 or (N == 1 or N == 3) and (K == 1 or K == 3)) and p != 3:
            return False
        if p % 2 > 0:
            if N % 2 == 0 and K % 2 == 0:
                return f(N - 4, K - 4, p + 1) and f(N / 2, N / 2, p + 1) and f(K / 2, K / 2, p + 1)
            elif N % 2 == 0:
                return f(N - 4, K - 4, p + 1) and f(N / 2, N / 2, p + 1)
            elif K % 2 == 0:
                return f(N - 4, K - 4, p + 1) and f(K / 2, K / 2, p + 1)
            else:
                return f(N - 4, K - 4, p + 1)
        else:
            if N % 2 == 0 and K % 2 == 0:
                return f(N - 4, K - 4, p + 1) or f(N / 2, N / 2, p + 1) or f(K / 2, K / 2, p + 1)
            elif N % 2 == 0:
                return f(N - 4, K - 4, p + 1) or f(N / 2, N / 2, p + 1)
            elif K % 2 == 0:
                return f(N - 4, K - 4, p + 1) or f(K / 2, K / 2, p + 1)
            else:
                return f(N - 4, K - 4, p + 1)


for K in range(1, 100):
    if f(28, K, 0):
        print(K)
