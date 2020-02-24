import math
from canvas import Picture, Color
from line import Line
from matrix import Matrix

m = Matrix()

print("Testing addEdge: adding (1,2,3) and (4,5,6) to m")
m.addEdge((1,2,3), (4,5,6))
m.print()
print()

print("Testing ident: ")
i = Matrix()
i.ident()
i.print()
print()

print("Multiplying i and m")
Matrix.multiply(i, m)
m.print()
print()

print("Multiplying by non-identity matrix")
print("i:")
i.content = [[1.0, 4.0, 7.0, 10.0], [2.0, 5.0, 8.0, 11.0], [3.0, 6.0, 9.0, 12.0], [1, 1, 1, 1]]
i.print()
print("m:")
m.print()
print("after multiplication:")
Matrix.multiply(i, m)
m.print()
print()


