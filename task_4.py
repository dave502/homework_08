from abc import ABC, abstractmethod


# класс - родитель для дочерних классов оргтехники
class OfficeEquipment(ABC):
    # tuple состояний техники
    __states = ('out of service', 'in work')
    # текущий статус
    _status = __states[1]

    def __init__(self, receipt_date, equipment_id):
        # дата ввода в эксплуатацию
        self.receipt_date = receipt_date
        # инвентаризационный номер
        self.__uid = equipment_id

    def __repr__(self):
        return self.__class__.__name__ + " " + self.uid

    def _get_state(self, i: int):
        return self.__states[i]

    @abstractmethod
    def set_status(self, status):
        pass

    # инвентаризационный номер
    @property
    def uid(self):
        return self.__uid

    @uid.setter
    def uid(self, uid):
        if uid.isalnum():
            self.uid = uid


# класс склада
class Store:
    # подразделения
    departments = []
    # сотрудники
    employees = []
    # офисное оборудование
    office_equipment = {}
    address = ''
    phone = ''

    def __init__(self, name):
        # имя компании склада
        self.__name = name

    @property
    def name(self):
        return self.__name

    def add_departments(self, *departments):
        """ добавить подразделение склада

        :param departments: подразделения
        :return:
        """

        for dep in departments:
            self.departments.append(dep)

    def add_employees(self, *employees):
        """ добавить сотрудников склада

        :param employees: сотрудники
        :return:
        """
        self.employees.append(employees)

    def add_office_equipment(self, equipment_dict):
        """ добавить оргтехнику на склад

        :param equipment_dict: dict - {'отдел':[list of equipment],....}
        :return:
        """
        for eq_el in equipment_dict.items():
            # объединение существующего списка оргтехники (если он есть) и добавляемого списка
            try:
                eq_el[1].extend(self.office_equipment[eq_el[0]])
            except Exception:
                pass
            # обновление словаря оргтехники
            self.office_equipment[eq_el[0]] = eq_el[1]

    def move_office_equipment(self, equipment_id, new_department=' '):
        """ переместить оргтехнику в отдел

        :param equipment_id: str - инвентаризационный номер оргтехники
        :param new_department: str - новый отдел
        :return:
        """

        # поиск оргтехники по uid в словаре принадлежности оргтехники к отделам
        for dep in self.office_equipment.keys():
            equipment = list(filter(lambda eq: eq.uid == equipment_id, self.office_equipment[dep]))
            # если объект с uid найден
            if len(equipment):
                # добавляем в список нужного отдела
                self.office_equipment[new_department].append(equipment[0])
                # удаляем из в списка старого отдела
                self.office_equipment[dep].remove(equipment[0])

    def set_store_contacts(self, address='', phone=''):
        """ добавить контактные данные склада

        :param address:
        :param phone:
        :return:
        """
        self.phone = phone
        self.address = address
