from re import A


class Calci:

    def __init__(self,
        a = 0,
        b = 0
    ) -> None:
        self.a = a 
        self.b = b

    def addition(self):
        return self.a + self.b

    def subraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b
