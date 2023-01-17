class switch:
    def __init__(self, value):
        self.value = value
        self.flag = False

    def case(self, value_2, func):
        if (self.value == value_2):
            func()
            self.flag = True

    def default(self, func):
        if (self.flag == False):
            func()

class pointer:
    def __init__(self, value):
        self.lst = [value]

    def get(self):
        return self.lst[0]

    def change(self, value):
        self.lst[0] = value

    def swap(self, pointer2):
        temp = self.get()
        self.change(pointer2.get())
        pointer2.change(temp)