# Use the pass keyword when you do not want to add any other properties or methods to the class.

# inheritance
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#  super().__init__(fname, lname)
# parent_name. __init__(fname, lname)

# iterator vs iterable

# global to change variable scope

# access modifiers
# double underscore __private
# single underscore _protected


# switch using dict

def case1():
    print('case 1 is selected')
def case2():
    print('case 2 is selected')
def case3():
    print('case 3 is selected')

switch = {
    1: case1,
    2: case2,
    3: case3,
}

try:
    seleted_case = int(input('enter a number '))

    selected_function = switch.get(seleted_case)
    if selected_function:
        selected_function()
    else:
        print('invalid case')
except ValueError:
    print("Invalid input ")