class ZeroDivErr(Exception):
    def __init__(self, message):
        super(ZeroDivErr, self).__init__(message)


try:
    i = int(input('Введите делитель: '))

    if i == 0:
        raise ZeroDivErr('Ошибка деления на 0')

    print(f'результат деления 100 на {i} = {100 / i}')
except ZeroDivErr as ex:
    print(ex)
except ValueError as ex:
    print(ex)
