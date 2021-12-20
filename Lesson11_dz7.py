import random


class ComplexNum:
    def __init__(self):
        self.x = complex(random.random())

    def __str__(self):
        return f'{self.x}'

    def __add__(self, other):
        return f'Сложение комплексных чисел {self.x + other.x}'

    def __mul__(self, other):
        return f'Умножение комплексных чисел {self.x * other.x}'


c1 = ComplexNum()
c2 = ComplexNum()
print(c1)
print(c2)
print(c1 + c2)
print(c1 * c2)
