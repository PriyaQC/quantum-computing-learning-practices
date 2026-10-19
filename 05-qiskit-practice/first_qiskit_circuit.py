#first_qiskit_circuit 
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a circuit with one qubit and one classical bit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Display the circuit
print(qc.draw())

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = simulator.run(qc, shots=1000).result()

# Print measurement counts
counts = compiled_circuit.get_counts()
print("Measurement counts:", counts)

#no gate
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a circuit with one qubit and one classical bit
qc = QuantumCircuit(1, 1)

# Measure the qubit
qc.measure(0, 0)

# Display the circuit
print(qc.draw())

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = simulator.run(qc, shots=1000).result()

# Print measurement counts
counts = compiled_circuit.get_counts()
print("Measurement counts:", counts)

#two harmard gates
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a circuit with one qubit and one classical bit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate
qc.h(0)
qc.h(0)
# Measure the qubit
qc.measure(0, 0)

# Display the circuit
print(qc.draw())

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = simulator.run(qc, shots=1000).result()

# Print measurement counts
counts = compiled_circuit.get_counts()
print("Measurement counts:", counts)