class Abacus:
    def __init__(self):
        self.units = 0
        self.tens = 0

    def set_number(self, num):
        self.units = num % 10
        self.tens = num // 10

    def get_number(self):
        return self.tens * 10 + self.units

    def add(self, value):
        self.units += value

        if self.units >= 10:
            carry = self.units // 10
            self.units = self.units % 10
            self.tens += carry

    def subtract(self, value):
        self.units -= value

        if self.units < 0:
            borrow = (-self.units + 9) // 10
            self.units += borrow * 10
            self.tens -= borrow