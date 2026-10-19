#matplotlib
import numpy as np 
import matplotlib.pyplot as plt 

bell_state = np.array([1,0,0,1])/np.sqrt(2)
probs = np.abs(bell_state)**2

labels  = ["00","01","10","11"]

plt.bar(labels,probs)
plt.xlabel("Measurement outcome")
plt.ylabel("Probability")
plt.title("Bell state: Measurement Probabilities")
plt.ylim(0,1)
plt.savefig("bell_state_probabilities.png",dpi = 150)
plt.show()