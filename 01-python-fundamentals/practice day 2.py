probability = 0.7

if probability > 0.5 :
    print("More likely")
else :
    print("Less likely")


#for elif
probability = 0.5 
if  probability > 0.5 :
    print("More Equally") 
elif probability == 0.5 :
    print("Equal likely") 
else :
    print("Less likely")         

#task 1
probability = 0.8 
if probability > 0.7 :
    print("High probability")    
elif probability >= 0.3 :
    print("Medium probability")    
else :
    print("Less probability")    

#task 2
x = 10
if x > 0 :
    print("Positive")    
elif x == 0 :
    print("Zero")    
else :
    print("Negative")

#task 3
probability_0 = 0.4 
probability_1 = 0.6
if probability_0 > probability_1 :
    print("Outcome 0 is more probable")    
elif probability_1 > probability_0 :
    print("Outcome 1 is more probable")   
else :
    print("Both outocmes are equally probable")     

#Lists
probabilities = [0.2,0.5,0.3]    
print(probabilities[0])
print(probabilities[1])
print(probabilities[2])

#Task 4
numbers = [2,4,6,8,10]
print(numbers[0])
print(numbers[2])
print(numbers[4])

#Task 5
probabilities = [0.1,0.2,0.3,0.4]
print(probabilities[0])
print(probabilities[1])
print(probabilities[2])
print(probabilities[3])

#Task 6
amplitudes = [0.5,0.5]
prob_0 = amplitudes[0]**2
prob_1 = amplitudes[1]**2
probabilities = [prob_0,prob_1]
print(probabilities)

#Loops
probabilities = [1,2,3,4]
for p in probabilities :
       print(p)

#Task 7
numbers = [1,2,3,4,5]    
total_sum = 0
for num in numbers :
    total_sum += num
    print(total_sum)

#Task 8
probabilities = [1,2,3,4,5]
for p in probabilities :
       print(p)

#Task 9
amplitudes = [0.2,0.4,0.6,0.8]   
for amp in amplitudes :
    print(amp**2) 

#Task 10
measurements = [0,1,0,1,1,0,1,1,0,1]  
count_zeros = 0 
for measurement in measurements :
    if measurement == 0 :
        count_zeros += 1 
        
print(count_zeros)  


