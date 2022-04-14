# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random
import string

def char_range(start, end):
    for char in range(ord(start), ord(end)):
        yield chr(char)
    # print(chr(char), ord(start), ord(end))

def randomizer(min, max, start, end):
    a = random.randint(min, max)
    b = random.triangular(min, max)
    letters = char_range(start, end)
    print(letters)
    c = random.choice(str(letters))
    print(str(letters))
    return a, b, c

if __name__ == '__main__':
    min = int(input('min = '))
    max = int(input('max = '))
    a = input('Буква 1: ')
    b = input('Буква 2: ')
    print(randomizer(min, max, a, b))