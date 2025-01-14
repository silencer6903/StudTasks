

def class_log(lst):
    def decorator(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for item, v in methods.items():
            setattr(cls, item, log_method_decorator(v))
        return cls

    def log_method_decorator(param):
        def wrapper(*args, **kwargs):
            lst.append(param.__name__)
            return param(*args, **kwargs)
        return wrapper
    return decorator














vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


s = Vector(10, 15)
s[0] =10002002
s[1 ]
print(vector_log)







