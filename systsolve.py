#using pseudo inverse: leads to the shortest solution 
import numpy

x = int(input("x départ:"))
y = int(input("y départ:"))

x_ar = int(input("x départ:"))
y_ar = int(input("y départ:"))

a = numpy.array([[1,1, -1, -1, 2, 2, -2, -2], [2, -2, 2, -2, 1, -1, 1, -1]]) # lets define <a>

b = numpy.array([x_ar-x,y_ar-y])

sol = numpy.linalg.pinv(a).dot(b)

A = numpy.linalg.pinv(a)
coefs = A.dot(b)
print(coefs)
print(sol)