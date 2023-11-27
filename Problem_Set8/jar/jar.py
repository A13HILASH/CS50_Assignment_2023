class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._cap = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"    

    def deposit(self, n):
        if n > self._cap:
            raise ValueError
        if self.size + n > self._cap:
            raise ValueError
        self._size = self._size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size = self._size - n

    @property
    def capacity(self):
        return self._cap

    @property
    def size(self):
        return self._size 
#Driver
jar = Jar()
jar.deposit(4)
jar.withdraw(2)
print(jar)