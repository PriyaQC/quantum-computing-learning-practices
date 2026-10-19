#Probability analyzer
import math

amplitudes = [1/math.sqrt(2),1/math.sqrt(2)]

def probability(amplitude):
    return abs(amplitude**2)

for amplitude in amplitudes:
    print(probability(amplitude)) 

probabilities = []
for amplitude in amplitudes:
    probabilities.append(probability(amplitude))

print(probabilities)
print(sum(probabilities))   

for amplitude in amplitudes :
    if sum(probabilities) == 1:
        print ("State is normalized")
    else :
        print("State is NOT normalized")

#Bonus Challenge
import math
amplitudes = [1/math.sqrt(3),1/math.sqrt(3),1/math.sqrt(3)]

def probabilty(amplitude):
    return abs(amplitude**2)

for amplitude in amplitudes:
    print(probability(amplitude)) 

probabilities = []
for amplitude in amplitudes :
    probabilities.append(probability(amplitude))

print(probabilities)
print(sum(probabilities))

#Bonus Challenge 2
amplitudes = [0.5,0.5]

def probability(amplitude):
    return abs(amplitude**2)

for amplitude in amplitudes:
    print(probability(amplitude))  

probabilities = []
for amplitude in amplitudes :
    probabilities.append(probability(amplitude))   

print(probabilities)   
print(sum(probabilities))

for amplitude in amplitudes:
    if sum(probabilities) == 1 :
        print("State is normalized")
    else:
        print("State is NOT normalized")    




