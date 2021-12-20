class MyException:
    def __init__(self, num):
        self.num = num

        try:
            int(num)
        except (ValueError, TypeError):
            return print('Параметр не является числом')
        else:
            num_list.append(num)
            return

            print('Элемент добавлен')


num_list = []
while True:

    num = input("Введи число или напиши stop ")
    if num == 'stop':
        print(num_list)
        break
    MyException(num)
