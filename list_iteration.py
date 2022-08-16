import sys
# Deak Windy Luke Biggs
# items = ["Deak", "Windy", "Luke", "Biggs"]

items = sys.argv
items.pop(0)

print("These are the items on my grocery list:")
for x in range (len(items)):
    print (f"{x+1}. {items[x]}")