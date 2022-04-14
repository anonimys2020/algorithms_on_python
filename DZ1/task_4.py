# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
import string
def check(a, b):
    alphabet = list(string.ascii_lowercase)
    a_id = 0
    b_id = 0
    for i in alphabet:
        if a == i:
            a_id += 1
            break
        else:
            a_id += 1
    for i in alphabet:
        if b == i:
            b_id += 1
            break
        else:
            b_id += 1
    res = b_id - a_id - 1
    return a_id, b_id, res, len(alphabet)

if __name__ == '__main__':
    a = input()
    b = input()
    print(check(a, b))