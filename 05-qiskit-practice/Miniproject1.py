#Miniproject 
import numpy as np 
zero_zero = np.array([1,0,0,0])
H = (1/np.sqrt(2)) * np.array([
    [1,1],
    [1,-1]
])
I = np.eye(2)
CNOT = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
])
after_h = np.kron(H,I) @ zero_zero
bell_state = after_h @ CNOT
print(bell_state)
probabilities = np.abs(bell_state)**2
print(probabilities)
total_probability = np.sum(probabilities)
print(total_probability)
if np.isclose(total_probability,1.0):
    print("state is normalized")
else:
    print("state is NOT normalized")

def entanglement_test(state):
    bell_state = state.reshape(2,2)
    determinant = np.linalg.det(bell_state)
    return not np.isclose(determinant,0)
print(entanglement_test(bell_state))

#Applying Hardmard gate to the first qubit state of the bell state
transformed = np.kron(H,I) @ bell_state
print(transformed)
print(entanglement_test(transformed))

