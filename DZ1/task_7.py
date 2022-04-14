# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.
if __name__ == '__main__':
    year = int(input())
    if year % 4 == 0:
        print(True)
    else:
        print(False)