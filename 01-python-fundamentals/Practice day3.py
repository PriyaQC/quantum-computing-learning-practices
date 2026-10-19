#Practice day3
#Task 1
def cube(x):
    print(x**3)

cube(2)
cube(3) 
cube(5)
cube(10)   
#Task 2
def add(a,b):
    return a + b 

result = add(5,3)    
print(result)
result = add(10,20)
print(result)

#Task 3 

import math
def probability(amplitude):
    return abs(amplitude)**2

result = probability(1/math.sqrt(2))
print(result)

#Task 4

import math
def probability(amplitude):
    return abs(amplitude)**2

result = probability(1/math.sqrt(3))    
print(result)

#Task 5 
import math

vectors = [(3,4),(5,12),(8,15)]

def vector_magnitude(x,y):
    return math.sqrt(x**2+y**2)

for x,y in vectors :
    print(vector_magnitude(x,y))    

#Task 6
import math    

vectors = [(2,3,6),(1,2,2)]

def vector_magnitude(x,y,z):
    return math.sqrt(x**2+y**2+z**2)

for x,y,z in vectors :
    print(vector_magnitude(x,y,z))    