# Data types in Python

# Type Hints
A: bytes = 5
B: int = 5
C: float = 5.0
D: chr = 5
E: str = "5"
F: bool = True 
G: list = [1, 2, 3] #Dynamic list
H: tuple = (1, 2, 3) #Static tuple
I: set = {1, 2, 3} #Unordered collection of unique elements
J: dict = {"one": 1, "two": 2, "three": 3} #Key-value pairs
K: tuple = ( (1, 2, 3), (4, 5, 6), (7, 8, 9) ) #Nested tuple
print("Data types using type hints:")
print("A is of type:", type(A))
print("B is of type:", type(B))
print("C is of type:", type(C))
print("D is of type:", type(D))
print("E is of type:", type(E))
print("F is of type:", type(F))
print("G is of type:", type(G))
print("H is of type:", type(H))
print("I is of type:", type(I))
print("J is of type:", type(J))

#Type casting
a = bytes(5)
b = int(5)
c = float(5.0)
d = chr(5)
e = str("5")
f = bool(True)
g = list([1, 2, 3])
h = tuple((1, 2, 3))
i = set({1, 2, 3})
j = dict({"one": 1, "two": 2, "three": 3})
k = ( (1, 2, 3), (4, 5, 6), (7, 8, 9) )
print("Data types using type casting:")
print("a is of type:", type(a))
print("b is of type:", type(b))
print("c is of type:", type(c))
print("d is of type:", type(d))
print("e is of type:", type(e))
print("f is of type:", type(f))
print("g is of type:", type(g))
print("h is of type:", type(h))
print("i is of type:", type(i))
print("j is of type:", type(j))