import task_4
import datetime


# создание классов - наследников Оргтехники
class Printer(task_4.OfficeEquipment):
    def start_print(self):
        pass

    def set_status(self, status):
        self._status = super()._get_state(status)


class Scaner(task_4.OfficeEquipment):
    def start_scan(self):
        pass

    def set_status(self, status):
        self._status = super()._get_state(status)


class Xerox(task_4.OfficeEquipment):
    def start_copy(self):
        pass

    def set_status(self, status):
        self._status = super()._get_state(status)


# создание объектов оргтехники
printer_1 = Printer('01-11-2019', '001')
printer_2 = Printer('01-12-2019', '002')
printer_3 = Printer('10-01-2020', '003')
scaner_1 = Scaner('02-11-2019', '004')
xerox_1 = Xerox('05-02-2020', '005')
xerox_2 = Xerox('06-02-2020', '006')

# создание объекта склада
store = task_4.Store('Склад')

# добавление отделов на склад
store.add_departments('бухгалтерия', 'главный оффис', 'отдел маркетинга', 'отдел продаж')
store.add_departments('отдел закупок')

# добавление оргтехники на склад
store.add_office_equipment({'бухгалтерия': [printer_1, printer_2], 'главный оффис': [scaner_1],
                            'отдел маркетинга': [printer_3], 'отдел продаж': [xerox_1]})
store.add_office_equipment({'бухгалтерия': [xerox_2]})

# перемещение оргтехники по инвентаризационному номеру в другой отдел
store.move_office_equipment('006', 'главный оффис')

print(store.office_equipment)

# предоставляем возможность ввести данные пользователю, проверяем введённые данные
while True:

    uid = input('Введите инветаризационный номер оргтехники: ')
    if not uid.isalnum():
        print('Вы ввели некорректный номер. Попробуйте ещё раз.')
        continue
    elif not len(uid):
        break  # пустое значение -> выход из цикла

    eq = input('Введите вид техники (0 - принтер, 1 - сканер, 2 - ксерокс): ')
    try:
        if not (0 <= int(eq) <= 2):
            print('Вы ввели некорректное счисло. Попробуйте ещё раз.')
            continue
    except ValueError as ex:
        print(ex)
    eq_class = [Printer, Scaner, Xerox][int(eq)]

    dep_num = input(f'Введите номер отдела ({dict(enumerate(store.departments))}): ')
    try:
        dep = dict(enumerate(store.departments))[int(dep_num)]
    except KeyError:
        print('Вы ввели некорректный номер отдела. Попробуйте ещё раз.')
        continue

    print(f'Будет добавлен {eq_class.__name__} c id {uid} в отдел {dep}')
    store.add_office_equipment({dep: [eq_class(datetime.datetime.today().strftime("%d-%m-%Y"), uid)]})

    print(store.office_equipment)
