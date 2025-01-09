



class Check:
    def __init__(self):
        pass

    def __call__(self, func):
        def wrapper(self, other):
            d = {'__add__': lambda s: s + other,
                 '__sub__': lambda s: s - other,
                 '__rsub__': lambda s: other - s,
                 '__mul__': lambda s: s * other,
                 '__truediv__': lambda s: s / other,
                 '__rtruediv__': lambda s: other / s,
                 }

            if not isinstance(other, (int, float)):
                raise TypeError


            match func:
                case s if s.__name__ in ('__rsub__', '__rtruediv__'):
                    return New_lst([*map(d[s.__name__], self.lst)])
                case s if s.__name__ in d:
                    return New_lst([*map(d[func.__name__], self.lst)])
                case s if s.__name__.strip('__')[0] == 'r':
                    return d[s.__name__.replace('r', '')](self)
                case s if s.__name__.strip('__')[0] == 'i':
                    self.lst = [*map(d[s.__name__.replace('i', '', 1)], self.lst)]
                    return self

        return wrapper


class New_lst:
    def __init__(self, lst):
        self.lst = lst


    @property
    def lkl(self):
        return self.lst




    @Check()
    def __add__(self, other):
        pass

    @Check()
    def __radd__(self, other):
        pass

    @Check()
    def __iadd__(self, other):
        pass

    @Check()
    def __sub__(self, other):
        pass

    @Check()
    def __rsub__(self, other):
        pass

    @Check()
    def __isub__(self, other):
        pass

    @Check()
    def __mul__(self, other):
        pass

    @Check()
    def __rmul__(self, other):
        pass

    @Check()
    def __imul__(self, other):
        pass

    @Check()
    def __truediv__(self, other):
        pass

    @Check()
    def __rtruediv__(self, other):
        pass

    @Check()
    def __itruediv__(self, other):
        pass






a = New_lst([1, 2, 3, 4, 5, 7, 10, 3, 4, 5, 6, 7, 8, 9, 10])
b = New_lst([1, 2, 3, 4, 5])
s = 9 / a
a /= 2
print(a.lst)
print(s.lst)




