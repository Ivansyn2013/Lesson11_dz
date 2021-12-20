class Warehouse:
    dict1 = {}

    def __init__(self, cls, nums):
        try:
            int(nums)
        except (ValueError, TypeError):
            return ('Неправильно введено количество')
        else:
            self.nums = nums
            cls.dict_in[cls.name] = nums
            if self.dict1.get(cls.types) == None:
                self.dict1.update({cls.types: cls.dict_in})
            else:
                self.dict1[cls.types] = cls.dict_in

    def get_out(self, types, name, nums, department):
        if int(self.dict1[types][name]) < int(nums):
            print(f'На складе {name} столько нет')

        else:
            print(self.dict1[types][name])
            self.dict1[types][name] = int(self.dict1[types][name]) - int(nums)
            print(f'{nums} {name} уехало в {department}')

    def __str__(self):
        return f'На складе:{self.dict1} '


class OfficeTech:
    def __init__(self, name, types):
        self.name = name
        self.types = types


class Printer(OfficeTech):
    dict_in = {}

    def __init__(self, name):
        super().__init__(name, types)
        self.types = 'Printer'
        self.paper = 'A4'
        self.dict_in[name] = []


class Scaner(OfficeTech):
    dict_in = {}

    def __init__(self, name):
        self.pix = 300
        self.types = 'Scaner'
        super().__init__(name, types)
        self.dict_in[name] = []


class Xerox(OfficeTech):
    dict_in = {}

    def __init__(self, name):
        self.copy = 1
        self.types = 'Xerox'
        super().__init__(name, types)
        self.dict_in[name] = []


while True:
    start = input('Введите объект: имя, тип, количество :')
    if start == 'забрать':
        start = input('Укажи тип имя и количество и куда: ')
        try:
            types, name, nums, dep = (start.split(' '))
        except ValueError:
            print('Ошибка в указании аргументов')
            continue
        else:
            if int(nums) < 0:
                print("количество может быть только целое и положительное")
                continue
            w1.get_out(types, name, nums, dep)
            continue
    if start == 'stop':
        break
    try:
        name, types, numbs = (start.split(' '))
    except ValueError:
        print('Неправильно введены значения')
    if types == 'printer':
        w1 = Warehouse(Printer(name), numbs)
        print(w1)
    if types == 'scaner':
        w1 = Warehouse(Scaner(name), numbs)
        print(w1)
    if types == 'xerox':
        w1 = Warehouse(Xerox(name), numbs)
        print(w1)
