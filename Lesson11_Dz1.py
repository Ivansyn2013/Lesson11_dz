class Date:
    def __init__(self, date_s):
        self.date_s = str(date_s)
        Date.valid_date(date_s)

    @classmethod
    def get_date(cls, date_s):
        date_s = str(date_s)
        date_list = []
        date_list = list(map(int,(date_s.split('-'))))
        return print(f' День {date_list[0]} Месяц {date_list[1]} Год {date_list[2]}')

    @staticmethod
    def valid_date(date_s):
        date_s = str(date_s)
        date_list = []
        date_list = list(map(int, (date_s.split('-'))))
        if len(date_list) != 3:
            return print('Неправильно зажан форма даты')

        if date_list[0] not in range(1,32) :
            return print('Неправильно задан день')


        if date_list[1] not in range(1,13) :
            return print('Неправильно задан месяц')

        if date_list[2] not in range(1900,2050) :
            return print('Неправильно задан год')



Date.get_date('22-10-2222')
d1 = Date('22-102-22222')