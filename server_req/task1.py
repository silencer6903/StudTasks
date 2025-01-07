from curses import wrapper
from random import randrange, choice, sample
from string import ascii_lowercase as low, digits, hexdigits


class LenValidator:
    def __init__(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len

    def __call__(self, text,  *args, **kwargs):
        return self.min_len <= len(text) <= self.max_len

class LoginForms:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for i in self.validators:
            if not i(self.login) or not i(self.password):
                return False

        return True

















class RenderDigit:

    def __call__(self,st, *args, **kwargs):
        if set(st).issubset(digits) or st[0] == '-' and set(st[1:]).issubset(digits):
            return int(st)
        return


class ImputDigit:
    def __init__(self, render):
        self.render = render

    def __call__(self,func,  *args, **kwargs):
        def wrapper():
            return [*map(self.render, func().split())]
        return wrapper






render = RenderDigit()

@ImputDigit(render)
def foo():
    return input("Input Integer numbers: ")

print(foo())