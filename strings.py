import sys


'''
To complete the Trial of Words, you must manipulate a string of text to enhance its excitement. 
    Take the first command line argument to your script and transform it in the following ways:

Convert it to all upper case letters
Append three exclamation points
After you transform the string in this way, print the new string to the console
'''
in_arg = sys.argv
in_arg.pop(0)



if len(in_arg) > 0:
    in_frase = ' '.join(str(x) for x in in_arg)
    out_frase = in_frase.upper() + "!!!"
    print(out_frase) 
else:
    print("Missing arguments, please execute again with arguments in command line")

    

