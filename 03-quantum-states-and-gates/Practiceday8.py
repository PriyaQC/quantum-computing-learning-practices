#Practiceday8
#Transpose
import numpy as np
A = np.array([
    [1,2],
    [3,4]
])
print(A.T)
#3x2matrix
import numpy as np 
B = np.array([
    [1,2],
    [3,4],
    [5,6]
])
transpose = B.T
print(transpose)
print(B.shape)
print(transpose.shape)
#Conjugatetranspose
import numpy as np
A = np.array([
    [1+2j,3],
    [4j,5-1j]
])
print(A.conj().T)
#unitary matrices
H = (1/np.sqrt(2))*np.array([
    [1,1],
    [1,-1]
])
identity = np.eye(2)
print(H.conj().T @ H)
print(identity)
#   Eigenvalues 
A = np.array([
    [1,0],
    [0,-1]
])
eigenvalues , eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)
X = np.array([
    [0,1],
    [1,0]
])
Z = np.array([
    [1,0],
    [0,-1]
])
H = np.array([
    [1,1],
    [1,-1]
])
zero = np.array([1,0])
one = np.array([0,1])
plus = H @ zero
print(X @ zero)
print(X @ one)
print(X @ plus)
print(Z @ zero)
print(Z @ one)
print(Z @ plus)
print(H @ zero)
print(H @ one)
print(H @ plus)

