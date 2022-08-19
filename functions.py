# v2
def hail_friend(friend):
    print(f"Hail, {friend}!")

def add_numbers(x,y):
    '''return the result of adding those two numbers together'''
    try:
        num_add = int(x) + int(y)
        return num_add
    except:
        raise ValueError("Expecting 2 integers")

if __name__ == '__main__':
    hail_friend('Jonathan Joestar')
    print(add_numbers(3,2))