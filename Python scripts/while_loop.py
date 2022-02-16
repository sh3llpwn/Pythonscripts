#!/bin/python3

"""
while loop also run as for but difference that in for loop you know number of times you want to run the loop, where as in while loop we give condition till which it will run.
"""

"""
syntax of while loop

condition_variable
while condition:
	code_here
	condition_variable_modification
"""
i = input("Enter a number : ")
i = int(i)					#condition_variable
while i != 0:
	print("Number is",i)		#code_here
	i = i - 1				#condition_variable_modification
	
print("while loop ended")
