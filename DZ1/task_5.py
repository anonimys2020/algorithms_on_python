# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string

def check(number):
    alphabet = [None] + list(string.ascii_lowercase)
    return alphabet[number] # n > 0, alphabet[0] = 'None'

if __name__ == '__main__':
    number = int(input())
    print(check(number))