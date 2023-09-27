class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self.amount = 0
        self.cookies = ""
        self.count = 0

    def __str__(self):
        while self.count < self.amount:
            self.cookies += "🍪"
            self.count += 1
        return self.cookies

    def deposit(self, n):
        self.amount += n
        if self.amount > self._capacity:
            raise ValueError

    def withdraw(self, n):
        if n > self.amount:
            raise ValueError
        self.amount -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.amount