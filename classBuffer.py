class Buffer:
    def __init__(self):
        self.list = []
        # конструктор без аргументов

    def add(self, *a):
        for i in a:
            self.list.append(i)
            while len(self.list) >= 5:
                print(sum(self.list[:5]))
                self.list = self.list[5:]
        # добавить следующую часть последовательности

    def get_current_part(self):
        return self.list
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
