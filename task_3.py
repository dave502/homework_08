# класс-исключение
class InvalidNumList(Exception):
    def __init__(self, message):
        super().__init__(message)

#  проверка содержимого списка на наличие только чисел
    @staticmethod
    def validate_num(num: str) -> bool:
        if num.isdigit():
            return True
        else:
            return False


user_list = []

while True:
    user_input = input('Введите елемент списка или пустое значение для завершения: ')

    # выход из цикла по пустому значению
    if not user_input:
        break

    try:
        # проверка введённого значения на число
        if not InvalidNumList.validate_num(user_input):
            raise InvalidNumList('Необходимо вводить только числа')
    except InvalidNumList as ex:
        print(ex)
        # продолжение цикла при исключении
        continue

    # добавить в список
    user_list.append(user_input)

print(user_list)
