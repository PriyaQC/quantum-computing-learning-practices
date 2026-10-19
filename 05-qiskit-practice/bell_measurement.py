#bell_measurement

import numpy as np

# Bell state |Phi+>
bell_state = np.array([
    1 / np.sqrt(2),
    0,
    0,
    1 / np.sqrt(2)
])

# Theoretical probabilities for |00>, |01>, |10>, |11>
probabilities = np.abs(bell_state) ** 2

print("Theoretical probabilities:", probabilities)

# Simulate 1000 two-qubit measurements
outcomes = ["00", "01", "10", "11"]

results = np.random.choice(
    outcomes,
    size=1000,
    p=probabilities
)

for outcome in outcomes:
    count = np.sum(results == outcome)
    print(
        outcome,
        "count:", count,
        "frequency:", count / 1000
    )

import matplotlib.pyplot as plt

plt.bar(outcomes, probabilities)
plt.xlabel("Measurement outcome")
plt.ylabel("Theoretical probability")
plt.title("Bell State Measurement Probabilities")
plt.ylim(0, 0.6)
plt.savefig("bell_state_probabilities.png")
plt.show()    