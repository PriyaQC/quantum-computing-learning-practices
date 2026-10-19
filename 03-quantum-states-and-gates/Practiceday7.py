#Practice day 7
import numpy as np
Z = np.array([1+2j,3+4j])
print(np.conjugate(Z))

#Inner product
u = np.array([1,2])
v = np.array([3,4])

inner = np.vdot(u,v)
print(inner)
#For Inner product complex
u = np.array([1+1j,2])
v = np.array([1,1j])
inner = np.vdot(u,v)
print(inner)

#Normalization
import numpy as np
psi = np.array([
    1/np.sqrt(2),
    1/np.sqrt(2)
])

print(np.vdot(psi,psi))
#Orthogonal states
import numpy as np  
zero = np.array([1,0])
one = np.array([0,1])

print(np.vdot(zero,one))
#Hardmard gate
H = (1/np.sqrt(2))*np.array([
    [1,1],
    [1,-1]
])
zero = np.array([1,0])
result = H @ zero
print(result)
probabilities = np.abs(result)**2
print(probabilities)
result1 = H @ zero
result2 = H @ result1
print(result2)
