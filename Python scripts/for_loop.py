#!/bin/python3 

# for loop is a way to repeat process for known number of times
# last value ie 10 here is ignored 
# range is a function which limits you values 

"""
syntax of for loop
for variable in range(start,end,step_size):
    code_here
"""
print("for loop with step size 1")
for i in range(1,10):
	print(str(i) + "th itteration i =",i)
print("\n")
print("for loop with step size 1 ended")

print("\n")

print("for loop with step size 2")
j=1
for i in range(1,10,2):
	print(str(j) + "th itteration i =",i)
	j = j + 1
print("\n")
print("for loop with step size 2 ended")

