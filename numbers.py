'''To complete the Trial of Numbers, 
your code must declare four variables which are the result of math operations 
performed on the two numbers passed in to your script as command line arguments. 
Use the following code as a starting point:'''

from logging import raiseExceptions
import sys

# This code reads in arguments and converts those inputs to decimal numbers
try:
    first_number = float(sys.argv[1])
    second_number = float(sys.argv[2])
except: 
    print("missing 2 numeric variables as arguments")
    exit()

# Your code goes here!
result_sum = first_number + second_number
result_difference = first_number - second_number
result_product = first_number * second_number
result_quotient = first_number / second_number

print(f"{first_number} plus {second_number} equals {result_sum}")
print(f"{first_number} minus {second_number} equals {result_difference}")
print(f"{first_number} multiplied {second_number} equals {result_product}")
print(f"{first_number} divided {second_number} equals {result_quotient}")