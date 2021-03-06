# 6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
# У треугольника сумма любых двух сторон должна быть больше третьей. Иначе две стороны просто "лягут" на третью и треугольника не получится.
def check(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник не существует"
    elif a != b and a != c and b != c:
        return "Разносторонний"
    elif a == b == c:
        return "Равносторонний"
    else:
        return "Равнобедренный"

if __name__ == '__main__':
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    print(check(a, b, c))