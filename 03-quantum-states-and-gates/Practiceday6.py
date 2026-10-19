#Practice day 6
import numpy as np
z = 3 + 4j
print(z)
print(abs(z))
#Task1
import  numpy as np
z1 = 1 + 2j
z2 = 2 - 3j

print(z1 + z2)
print(z1 * z2)
print(abs(z1))
print(abs(z2))
#Complex vectors
import numpy as np 
psi = np.array([
    1/np.sqrt(2),
    1j/np.sqrt(2)
])
print(np.abs(psi))
print(np.abs(psi)**2)

#Normalization
psi = np.array([
    1/np.sqrt(2),
    1j/np.sqrt(2)
])
probabilities = np.abs(psi)**2
total = np.sum(probabilities)
print(probabilities)
print(total)

#Matrix and Vector
import numpy as np 
A = np.array([
    [1,0],
    [0,-1]
])

psi = np.array([
    1/np.sqrt(2),
    1/np.sqrt(2)
])

result = A @ psi
print(result)

#Pauli x gate
import numpy as np
X = np.array([
    [0,1],
    [1,0]
])

zero = np.array([1,0])

result = X @ zero
print(result)
#For practice
import numpy as np
X = np.array([
    [0,1],
    [1,0]
])

one = np.array([0,1])

result = X @ one
print(result)
#Mini Experiment
import numpy as np 
X = np.array([
    [0,1],
    [1,0]
])

psi = np.array([
    1/np.sqrt(2),
    1/np.sqrt(2)
])

result = X @ psi
print(result)
#Mini project
import numpy as np 
zero = np.array([1,0])
one = np.array([0,1])

X = np.array([
    [0,1],
    [1,0]
])
print(X @ zero)
print(X @ one)
plus = np.array([
    1/np.sqrt(2),
    1/np.sqrt(2)
])
probability = np.abs(plus)**2
total = np.sum(probability)
print(probability)
print(total)

print(X @ plus)

#Bonus challenge
Z = np.array([
    [1,0],
    [0,-1]
])
zero = np.array([1,0])
one = np.array([0,1])
print(Z @ zero)
print(Z @ one)

plus = np.array([
    [1/np.sqrt(2)],
    [1/np.sqrt(2)]
])
print(Z @ plus)
probabilities = np.abs(plus)**2
total = np.sum(probabilities)
print(probabilities)
print(total)