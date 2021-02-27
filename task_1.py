class Date:
    def __init__(self, str_date: str):
        self.date = str_date

    @classmethod
    def list_date(cls, str_date: str) -> list:
        """# преобразование строки даты в список чисел

        :param str_date: str  «date-month-year»
        :return: list[date, month, year]
        """
        try:
            return [int(num) for num in str_date.split('-')]
        except Exception as ex:
            print(ex)

    @staticmethod
    def validate_date(list_date: list):
        """ проверка корректности даты

        :param list_date: list[date, month, year]
        :return:
        """

        result = False

        # класс для вывода ошибок
        class ValidateError(Exception):
            def __init__(self, message):
                super().__init__(message)

        try:
            # проверка года на положительное число
            year = int(list_date[2])
            if year < 0:
                raise ValidateError("Некорректное значение года")

            # словарь для проверки количества дней в месяце
            days_in_month = {'1': 31, '2': 28 if year % 4 else 29, '3': 31, '4': 30, '5': 31, '6': 30,
                             '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

            # проверка месяца на вхождение в пределы 1 - 12
            month = int(list_date[1])
            if (month < 1) or (month > 12):
                raise ValidateError("Некорректное значение месяца")

            # проверка дня на вхождение в пределы 1 - <количество дней в месяце>
            day = int(list_date[0])
            if (day < 1) or (day > days_in_month[str(month)]):
                raise ValidateError("Некорректное значение дня")

        except ValidateError as ex:
            print(ex)
        # исключение на ошибки преобразования и др.
        except Exception as ex:
            print(ex)
        # если исключений не было - дата является корректной
        else:
            result = True

        return result


date = Date('29-02-2020')
list_date = Date.list_date(date.date)

print(list_date)

if Date.validate_date(list_date):
    print(f'Дата {list_date} является корректной')
else:
    print(f'Дата не является корректной')
