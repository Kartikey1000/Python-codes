class Jar:
    def __init__(self,capacity=12):
        if not isinstance(capacity,int) or capacity<0:
            raise ValueError("Capacity must be a non negative integer")

        self._capacity= capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self,n):
        if n<0:
            raise ValueError("Can't deposit")
        if self._size +n > self._capacity:
            raise ValueError("Capacity exceeded")

        self._size +=n

    def withdraw(self,n):
        if n<0:
            raise ValueError("Negative cookies can't be taken")
        if n>self._size:
            raise ValueError("Not enough")
        self._size -=n

    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size

jar = Jar()

print(jar.capacity)
print(jar.size)

jar.deposit(3)

print(jar.size)
print(jar)