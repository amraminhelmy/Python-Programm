import LinkedLists

class Stack:
    def __init__(self):
        self._list = LinkedLists.LinkedList()

    def push(self, data):
        self._list.append(data)

    def pop(self):
        return self._list.pop()

    def is_empty(self):
        return self._list.is_empty()

Students = Stack()
Students.push("John")
Students.push("Alice")
Students.push("Bob")
print(Students.pop())  # Output: Bob
print(Students.is_empty())  # Output: False
Students.pop()  # Removes Alice
print(Students.pop())  # Output: John
print(Students.is_empty())  # Output: True