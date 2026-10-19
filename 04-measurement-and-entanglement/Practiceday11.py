#practiceday11
import numpy as np 
psi = np.array([1/np.sqrt(2),1/np.sqrt(2)])
probabilities = np.abs(psi)**2
print(probabilities)

#Simulating 1000 measurements
results = np.random.choice(
    [0,1],
    size = 1000,
    p=probabilities
)
count_0 = np.sum(results == 0)
count_1 = np.sum(results == 1)

print("number of 0 outcomes:", count_0 )
print("number of 1 outcomes:", count_1)

