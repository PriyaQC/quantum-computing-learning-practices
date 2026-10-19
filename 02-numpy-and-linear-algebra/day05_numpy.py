#day05_numpy.py 
import numpy as np 

print(np.__version__)

#Creating Numpy Arrays
import numpy as np 
a = np.array([1,2,3])
print(a)

#2D array
import numpy as numpy
matrix = np.array([
    [1,2],
    [3,4]
])
print(matrix)
#Indexing
import numpy as np
v = np.array([10,20,30])

print(v[0])
print(v[1])
print(v[2])

#for matrix 
import numpy as np
A = np.array([
    [1,2],
    [3,4]
])

print(A[0,0])
print(A[0,1])
print(A[1,0])
print(A[1,1])

#Shape 
import numpy as np
A = np.array([
    [1,2],
    [3,4]
])
print(A.shape) #row x column

B = np.array([
    [1,2,3],
    [4,5,6]
])
print(B.shape)

#Vector operation
import numpy as np
v = np.array([1,2,3])
print(v+v)
print(v*2)
print(v**2)

#Vector magnitude
v = np.array([3,4])
magnitude = np.linalg.norm(v)
print(magnitude)

#Matrix addition
A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])
print(A+B)

#Matrix multiplication
A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print(A @ B)
#Numpy vectors 
import numpy as np

v = np.array([3,4])
magnitude = np.linalg.norm(v)
print(magnitude)

#Qubit state
psi = np.array([
    1/np.sqrt(2),
    1/np.sqrt(2)
])
print(psi)

#Challange questions
psi = np.array([
    1/np.sqrt(2),
    1/np.sqrt(2)
])
magnitude = np.linalg.norm(psi)
print(magnitude)

probabilities = np.abs(psi**2)
print(probabilities)
