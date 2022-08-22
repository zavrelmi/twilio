import sys

try:
    sum_value = int(sys.argv[1]) + int(sys.argv[2])
except: 
    print("missing 2 numeric variables as arguments")
    exit()


if sum_value <= 0:
    print("You have chosen the path of destitution.")
elif sum_value > 100:
    print("You have chosen the path of excess.")
else:
    print("You have chosen the path of plenty.")