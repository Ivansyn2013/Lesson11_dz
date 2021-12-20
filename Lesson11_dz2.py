class MyException1(Exception):
    pass
class MyException:
    def get_division(self, x, y):
        try:
            res = x / y
            if x < 0:
                raise MyException1('Только положительные')
        except (MyException1, ZeroDivisionError) as err:
                print(err)

        else:
            return (f' Результат {res}')



d1= MyException()
d2 = MyException1()
x, y = map(int, (input('Введи два числа для деления, через пробел:')).split(' '))

print(d1.get_division(x,y))

try:
   res =  x / y
   if x < 0 :
       raise MyException1('Только положительные')
except (MyException1, ZeroDivisionError) as err:
    print(err)