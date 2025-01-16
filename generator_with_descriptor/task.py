

class FloatValue:
    @classmethod
    def chck_value(cls, value):
        if not isinstance(value, float):
            raise TypeError("Digit must be float type")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.chck_value(value)
        setattr(instance, self.name, value)

class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:
    def __init__(self, n, m):
        self._n = n
        self._m = m
        self.cels = [[0]*m for _ in range(n)]


    def add(self):
        for i in range(self._n):
            for j in range(self._m):
                obj = yield
                self.check_obj(obj)
                self.cels[i][j] = obj




    @classmethod
    def check_obj(cls, obj):
        if not isinstance(obj, Cell):
            raise TypeError("Object must be Cell")

    @property
    def n(self):
        return self._n

    @property
    def m(self):
        return self._m

import random


table = TableSheet(3, 5)
gen = table.add()
next(gen)
for i in range(3):
    for j in range(5):
        try:
            gen.send(Cell(float(random.randrange(1, 20))))
        except StopIteration:
            print("Ітерація завершена!")
print(*[[table.cels[i][j].value for j in range(5)] for i in range(3)], sep='\n')

