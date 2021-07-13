from numpy import array, column_stack
from numpy.linalg import det

X= array((3,2,1), dtype="f")
Y= array((2,3,2), dtype="f")
Z= array((1,1,3), dtype="f")
C= array((90,77,46), dtype="f")

x= det(column_stack((C,Y,Z)))/det(column_stack((X,Y,Z)))
y= det(column_stack((X,C,Z)))/det(column_stack((X,Y,Z)))
z= det(column_stack((X,Y,C)))/det(column_stack((X,Y,Z)))


print(f"x={round(x)}")
print(f"y={round(y)}")
print(f"z={round(z)}")
