class DynamicArray:
    def __init__(self, capacity=10, resize_factor=2):
        self.capacity = capacity
        self.resize_factor = resize_factor
        self.arr = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize()
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[index] = element
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        self.size -= 1
        self.arr[self.size] = None 

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate(self, k):
        k %= self.size
        self.arr = self.arr[-k:] + self.arr[:-k]

    def reverse(self):
        self.arr = self.arr[::-1]

    def append(self, element):
        if self.size == self.capacity:
            self._resize()
        self.arr[self.size] = element
        self.size += 1

    def prepend(self, element):
        self.insert(0, element)

    def merge(self, other_array):
        self.arr += other_array.arr
        self.size += other_array.size

    def interleave(self, other_array):
        result = []
        min_size = min(self.size, other_array.size)
        for i in range(min_size):
            result.append(self.arr[i])
            result.append(other_array.arr[i])
        if self.size > other_array.size:
            result += self.arr[min_size:]
        else:
            result += other_array.arr[min_size:]
        self.arr = result
        self.size += other_array.size

    def middle(self):
        if self.size == 0:
            return None
        return self.arr[self.size // 2]

    def index_of(self, element):
        for i in range(self.size):
            if self.arr[i] == element:
                return i
        return -1

    def split(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        arr1 = DynamicArray()
        arr1.arr = self.arr[:index]
        arr1.size = index
        arr1.capacity = index
        arr2 = DynamicArray()
        arr2.arr = self.arr[index:]
        arr2.size = self.size - index
        arr2.capacity = self.size - index
        return arr1, arr2

    def resize_factor(self, factor):
        if factor <= 1:
            raise ValueError("Resize factor must be greater than 1")
        self.resize_factor = factor

    def _resize(self):
        new_capacity = self.capacity * self.resize_factor
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity


array = DynamicArray()
array.append(1)
array.append(2)
array.append(3)
array.prepend(0)
print(array.arr[:array.size]) 
print(array.middle())
print(array.index_of(2))  
array.reverse()
print(array.arr[:array.size])  