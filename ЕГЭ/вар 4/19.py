def f(N, K, p):
    if N >= 0 and K >= 0:
        if ((N == 0 or K == 0 or (N == 3 or N == 1) and (K == 3 or K == 1))) and p == 2:
            return True
        elif ((N == 0 or K == 0 or (N == 3 or N == 1) and (K == 3 or K == 1))) and p != 2:
            return False
        if K % 2 == 0 and N % 2 == 0:
            return f(N - 4, K - 4, p + 1) or f(N / 2, N / 2, p + 1) or f(K / 2, K / 2, p + 1)
        elif K % 2 == 0:
            return f(N - 4, K - 4, p + 1) or f(K / 2, K / 2, p + 1)
        elif N % 2 == 0:
            return f(N - 4, K - 4, p + 1) or f(N / 2, N / 2, p + 1)
        else:
            return f(N - 4, K - 4, p + 1)
    else:
        return False


for K in range(1, 100):
    if f(28, K, 0):
        print(K)
