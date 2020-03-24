#using pseudo inverse: leads to the shortest solution, not useful in our case
import numpy as np

x = int(input("x départ:"))
y = int(input("y départ:"))

x_ar = int(input("x départ:"))
y_ar = int(input("y départ:"))

a = np.array([[1,1, -1, -1, 2, 2, -2, -2], [2, -2, 2, -2, 1, -1, 1, -1]]) # lets define <a>

b = np.array([x_ar-x,y_ar-y])

sol = np.linalg.pinv(a).dot(b)

print(sol)

a2 = np.array([1,1,2,2],[2,-2,1,-1])
b2 = np.array([0,1])
x2 = np.linalg.solve(a1,b1)
print(x2)