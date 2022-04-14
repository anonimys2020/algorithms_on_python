# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
def check(a, b, c):
    min_ = min(a, b, c)
    max_ = max(a, b, c)

    if a == min_ or a == max_:
        if b == min_ or b == max_:
            return c
        else:
            return b
    if b == min_ or b == max_:
        if c == min_ or c == max_:
            return a
        else:
            return c
    if c == min_ or c == max_:
        if a == min_ or a == max_:
            return b
        else:
            return a

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    print(check(a, b, c))