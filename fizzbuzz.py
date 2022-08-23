'''
Create a program that accepts any number of command line arguments. 
The arguments will be whole/integer numbers.
Your script will need to examine all these numbers and execute 
the following conditional logic:

If the number is divisible by 3, print the text: fizz
If the number is divisible by 5, print the text: buzz
If the number is divisible by both 3 and 5, print the text: fizzbuzz
If none of the above are true, print the number
'''
import sys

list_numbers = sys.argv
list_numbers.pop(0)

def tester(number):
    x = 0
    if (number % 3 == 0):
        x += 3
    if (number % 5 == 0):
        x += 5
    # Tis only works in python 3.10 and superior
    match x:
        case 8:
            return "fizzbuzz"
        case 5:
            return "buzz"
        case 3:
            return "fizz"
        case _:
            return number

for x in list_numbers:
    try:
        print(tester(int(x)))
    except: 
        print(f"{x} is not an integer")
        
