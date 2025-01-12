


class Obj:
    def __init__(self, data):
        self.data = data
        self.__next = None


    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


class Stack:
    def __init__(self):
        self.top = None
        self.cur = None

    def append(self, obj):

        if not self.top:
            self.top = obj
            self.cur = self.top

        self.cur.next = obj
        self.cur = obj

    def __getitem__(self, item):
        new_it = self.top
        i = 0
        while new_it:
            if item == i:
                return new_it
            new_it = new_it.next
            i+=1
        else:
            raise IndexError("Wrong index")

    def __setitem__(self, key, value):
        new_it = self.top
        new_o = value
        key = key-1 if key else 0
        i = 0
        while new_it:
            if key == i:
                new_o.next = new_it.next.next
                new_it.next = new_o

                break
            new_it = new_it.next
            i += 1
        else:
            raise IndexError("Wrong index")

s = Stack()
s.append(Obj("Hello"))
s.append(Obj("it"))
s.append(Obj("is"))
s.append(Obj("Python"))
print(s[0].data)
print(s[1].data)
print(s[2].data)
s[1] = Obj('Hi')
print(s[0].data)
print(s[1].data)
print(s[2].data)

















