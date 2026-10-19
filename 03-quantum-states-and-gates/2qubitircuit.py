#2 qubit ircuit
from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2)
print(qc.draw())

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create two qubits and two classical bits
qc = QuantumCircuit(2, 2)

# Prepare the state |10>
qc.x(0)

# Apply CNOT
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Display the circuit
print(qc.draw())

# Simulate 1000 runs
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()

print("Measurement counts:", result.get_counts())