class Obj:

    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.data = data
        self.ind = None


    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        self.__prev = obj


class LinkedList:
    def __init__(self):
        self.__root = None
        self.current = None
        self.ind = 0


    def add(self, obj: Obj) -> None:
        if self.__root is None:
            self.__root = obj
            self.current = self.__root
            obj.ind = self.ind

        obj.ind = self.ind
        self.ind += 1
        self.current.next = obj
        obj.prev = self.current
        self.current = obj

    def remove(self, obj):
        if self.__root is None:
            return

        ind = self.__root
        while ind:
            if ind.data == obj:
                m = ind.prev
                m.next = ind.next
                ind.next.prev = m
            ind = ind.next

    def pop(self):
        if self.__root is None:
            return None

        mn = self.current.prev
        mn.next = None
        self.current = mn

    def popleft(self):
        if self.__root is None:
            return

        mn = self.__root.next
        mn.prev = None
        self.__root = mn

    def show_data(self):
        if self.__root is None:
            return

        show = self.__root
        lst = []
        while show:
            lst.append(show.data)
            show = show.next

        return lst


s = ["Привіт", "Це", "Я", "Створив", "Цей", "Лінкед", "Ліст"]

link = LinkedList()
lst = []
for i in s:
    ind = Obj(i)
    lst.append(ind)
    link.add(ind)
    print(ind.ind)

print(link.show_data())
link.pop()
print(link.show_data())
link.popleft()
print(link.show_data())
link.popleft()
print(link.show_data())

link.remove("Цей")
print(link.show_data())


