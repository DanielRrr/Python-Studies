class ExtendedStack(list):
    def sum(self):
        # операция сложения
        if len(self) >= 2:
            a = self.pop()
            b = self.pop()
            self.append(a + b)

    def sub(self):
        # операция вычитания
        if len(self) >= 2:
            a = self.pop()
            b = self.pop()
            self.append(a - b)

    def mul(self):
        # операция умножения
        if len(self) >= 2:
            a = self.pop()
            b = self.pop()
            self.append(a * b)

    def div(self):
        # операция целочисленного деления
        if len(self) >= 2:
            a = self.pop()
            b = self.pop()
            self.append(a // b)
