# Найдите минимальное значение S,
# при котором одновременно выполняются два условия:
# — у Васи есть выигрышная стратегия, позволяющая ему выиграть
# первым или вторым ходом при любой игре Пети;
# — у Васи нет стратегии, которая позволит ему гарантированно выиграть первым 
# ходом.


def f(x, y, p):
    if x + y >= 77 and (p == 3 or p == 5):
        return True
    elif x + y < 77 and p == 5:
        return False
    elif x + y >= 77:
        return False
    if p % 2 == 1:
        return f(x + 1, y, p + 1) and f(x + y * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y + x * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) or f(x + y * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y + x * 2, p + 1)


for s in range(1, 68):
    if f(9, s, 1):
        print(s)
