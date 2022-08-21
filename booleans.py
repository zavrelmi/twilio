'''
Create a program that declares several boolean variables.
The third variable proper_greeting should be set to True 
if the first argument to your script is the exact string: For the glory of Python! 
'''
import sys

python_is_glorious = True
failure_is_option = False
proper_greeting = False

greeting = "For the glory of Python!"

try:
    if sys.argv[1] == greeting:
        proper_greeting = True
except:
    print("There is no argument passed")