#quantumfunctionsday3
#Function 1

amplitudes = [0.5,0.3,0.6]

def probability(amplitude) :
    return amplitude**2 

for amplitude in amplitudes:
    print(probability(amplitude))    

#Function 2
import math
vectors = [(4,5),(7,8)]

def vector_magnitude(x,y) :
    return math.sqrt(x**2+y**2)

for x,y in vectors :
    print(vector_magnitude(x,y))    

#Function 3
import math 
states = [(1/math.sqrt(2),1/math.sqrt(2))]    

def normalize_two_states(a,b) :
    return a**2 + b**2

for a,b in states :
    print(normalize_two_states(a,b))    

#Bonus challenge

normalities = [(5,2),(6,9),(1,7),(4,3)]

def check_normalization(a,b):
    return a**2 + b**2 

for a,b in normalities :
    if check_normalization(a,b) == 1 :
       print("state is normalized") 
    else :
        print("state is NOT normalized")   
