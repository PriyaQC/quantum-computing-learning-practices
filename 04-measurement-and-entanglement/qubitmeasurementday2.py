#Qubit_measurement

#count no.of items in it
measurements = [0,1,0,1,1,0,1,1,0,1]

num_measurement = len(measurements)
print(num_measurement)

count_zeros = 0
for measurement in measurements :
    if measurement == 0 :
        count_zeros += 1

print(count_zeros)  

count_ones = 0
for measurement in measurements :
    if measurement == 1:
        count_ones += 1
        

print(count_ones)        

probability_0 = count_zeros / num_measurement
probability_1 = count_ones / num_measurement
print(probability_0,probability_1)

# 1. Define the updated measurements list
measurements = [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

total_measurements = len(measurements)
print(total_measurements)

probability = {}
for outcome in set(measurements) :
    count = measurements.count(outcome)
    probability[outcome] = count / total_measurements
    print(probability[outcome])    