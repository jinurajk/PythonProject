import random
import math

print ("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print ("choice('A String') : ", random.choice('A String'))

#Randrange
# Select an even number in 100 <= number < 1000
print ("randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2))
# Select another number in 100 <= number < 1000
print ("randrange(100, 1000, 10) : ", random.randrange(100, 1000, 11))


# Random number
print ("random() : ", random.random())
print ("random() : ", random.random())

#Seed
print ("Random number with seed 10 : ", random.random())
random.seed( 10 )
print ("Random number with seed 10 : ", random.random())
random.seed( 11 )
print ("Random number with seed 10 : ", random.random())

#Shuffle list
list = [20, 16, 10, 5];
random.shuffle(list)
print ("Reshuffled list : ",  list)
random.shuffle(list)
print ("Reshuffled list : ",  list)

#Uniform
print ("Random Float uniform(5, 10) : ",  random.uniform(5, 10))
print ("Random Float uniform(7, 14) : ",  random.uniform(7, 14))


#Pie
print ("Pie value :", math.pi)

# e value
print ("E value :", math.e)

