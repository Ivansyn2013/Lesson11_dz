class MyException:
    def get_division(self,x,y):
        try:
            res = x/y
        except ZeroDivisionError:
            return print('Деление на ноль запрещено')
        else:
            return (f' Результат {res}')



d1= MyException()
x, y = map(int, (input('Введи два числа для деления, через пробел:')).split(' '))

print(d1.get_division(x,y))