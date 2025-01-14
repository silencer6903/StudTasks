class Observer:
    def update(self, data):
        print(f"Received update - Temp: {data.temp}, Press: {data.press}, Wet: {data.wet}")

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            del self.__observers[observer]

    def __notify_observer(self):
        for ob in self.__observers.values():
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()

class Data:
    def __init__(self, temp, press, wet):
         self.temp = temp
         self.press = press
         self.wet = wet



class TemperatureView(Observer):


    def update(self, data):
        print(f"Current temperature {data.temp}")

class PressureView(Observer):

    def update(self, data):
        print(f"Current pressure {data.press}")

class WetView(Observer):

    def update(self, data):
        print(f"Current wet {data.wet}")



subject = Subject()
tv = TemperatureView()
pr = PressureView()
wet = WetView()

subject.add_observer(tv)
subject.add_observer(pr)
subject.add_observer(wet)

subject.change_data(Data(23, 150, 83))

subject.remove_observer(wet)
subject.change_data(Data(24, 148, 80))




















