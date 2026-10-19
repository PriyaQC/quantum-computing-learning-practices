#Len()
measurements = [0,1,0,0,1,1]
print(len(measurements))

#range
for i in range(5):
    print(i)

for i in range(10):
    print(i)    

#sum()
numbers = [1,2,3,4,5]
total = sum(numbers)
print(total) 

#abs()
print(abs(5))
print(abs(-5))
print(abs(3+4j))

#task0
amplitudes = [1/2,1/2,1/2,1/2]

def probability(amplitude):
    return abs(amplitude**2)

for amplitude in amplitudes :
    print(probability(amplitude)) 

probabilities = []
for amplitude in amplitudes:
    probabilities.append(probability(amplitude))   

print(probabilities)
print(sum(probabilities))        