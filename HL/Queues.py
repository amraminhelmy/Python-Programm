import LinkedLists

class Queue:
    def __init__(self):
        self._list = LinkedLists.LinkedList()

    def enqueue(self, data):
        self._list.append(data)

    def dequeue(self):
        return self._list.pop_first()

    def is_empty(self):
        return self._list.is_empty()

Students = Queue()
Students.enqueue("John")
Students.enqueue("Alice")
Students.enqueue("Bob")
print(Students.dequeue())  # Output: John
print(Students.is_empty())  # Output: False
Students.dequeue()  # Removes Alice
print(Students.dequeue())  # Output: Bob
print(Students.is_empty())  # Output: True
