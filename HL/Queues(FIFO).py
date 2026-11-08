class Queue:
    def __init__(self):
        self._list = []

    def enqueue(self, data):
        self._list.append(data)

    def dequeue(self):
        return self._list.pop(0)

    def is_empty(self):
        return len(self._list) == 0

Students = Queue()
Students.enqueue("John")
Students.enqueue("Alice")
Students.enqueue("Bob")
print(Students.dequeue())  # Output: John
print(Students.is_empty())  # Output: False
Students.dequeue()  # Removes Alice
print(Students.dequeue())  # Output: Bob
print(Students.is_empty())  # Output: True
