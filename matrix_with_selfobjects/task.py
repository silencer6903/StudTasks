

class Integervalue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Just Integer numbers")

        return setattr(instance, self.name, value)

class Cellinteger:
    value = Integervalue()

    def __init__(self, start_value=0):
        self.value = start_value

class Tablevalues:
    def __init__(self, rows, cols, cell):
        if not isinstance(cell, Cellinteger) and not (set([type(rows), type(cols)]) == set([int])):
            raise ValueError("Not crate cell object")

        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    def __getitem__(self, item):
        if not isinstance(item, tuple) and len(item) == 2:
            raise ValueError("Key must be tuple")

        if not (set([type(item[0]), type(item[1])]) == set([int])):
            raise TypeError("Values in tuple must be Integer")

        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        if not isinstance(key, tuple) and len(key) == 2:
            raise ValueError("Key must be tuple")

        if not (set([type(key[0]), type(key[1])]) == set([int])):
            raise TypeError("Values in tuple must be Integer")

        self.cells[key[0]][key[1]].value = value




s = Tablevalues(5, 5, Cellinteger)
s[1, 2] = 10
s[1, 1] = 1
for rows in s.cells:
    for x in rows:
        print(x.value, end=' ')
    print()































