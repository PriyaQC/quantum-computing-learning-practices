#Practice day 9
import numpy as np 

zero = np.array([1,0])
one = np.array([0,1])

zero_zero = np.array([1,0,0,0])
zero_one = np.array([0,1,0,0])
one_zero = np.array([0,0,1,0])
one_one = np.array([0,0,0,1])

#Tensor products
zero = np.array([1,0])
one = np.array([0,1])
two_qubits = np.kron(zero,zero)
print(two_qubits)
print(np.kron(zero,one))
print(np.kron(one,zero))
print(np.kron(one,one))

#Combine superpositions
plus = np.array([
    1/np.sqrt(2),
    1/np.sqrt(2)
])

two_plus = np.kron(plus,plus)
print(two_plus)
print(np.abs(two_plus)**2)

#Application

H = (1/np.sqrt(2)) * np.array([
    [1,1],
    [1,-1]
])
I = np.eye(2)

H_first = np.kron(H,I)

print(H_first)
print(H_first.shape)
#apply it to |00>
zero_zero = np.array([1,0,0,0])

result = H_first @ zero_zero

print(result)
print(np.abs(result)**2)
zero_zero = np.array([1,0,0,0])
result = H_first @ zero_zero
print(result)
print(np.abs(result)**2)

#CNOT gate
C = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
])
zero_zero = np.array([1,0,0,0])
one_zero = np.array([0,0,1,0])

print(C @ zero_zero)
print(C @ one_zero)
#Bonuschallenge
zero_zero = np.array([1,0,0,0])
after_h = np.kron(H,I) @ zero_zero
bell = C @ after_h

print(bell)
print(np.abs(bell)**2)