# create a function
def divide():
    try:
        a = int(input("enter number 1 : "))
        b = int(input("enter number 2 :"))
        # error while dividing by zero 
        c = a/b
        print("answer is ", c)
    except ZeroDivisionError:
        print("cannot divide by zero")
        # calling method to try again
        print("try agian")
        divide()
    else:
        #lets you execute code when there is no error.
        print("no error")
    finally:
        # execute code, regardless of the result of the try- and except blocks.
        print("finally")

divide()

try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the exception
    print("You can't divide by zero.")

#Catching syntax error-
try:
    x = 10 / 0  # Intentional syntax error
except SyntaxError as e:
    print(f"Caught a SyntaxError: {e}")

#Catching name error-
try:
    result = undefined_variable
except NameError as e:
    print(f"Caught a NameError: {e}")

#Catching type error-
try:
    x = "5" + 2  # Attempting to add a string and an integer
except TypeError as e:
    print(f"Caught a TypeError: {e}")

#Catching value error-
try:
    value = int("abc")  # Trying to convert a non-integer string
except ValueError as e:
    print(f"Caught a ValueError: {e}")

#Catching division by zero error
try:
    result = 10 / 0  # Division by zero
except ZeroDivisionError as e:
    print(f"Caught a ZeroDivisionError: {e}")
#Catching FileNotFoundError -
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Caught a FileNotFoundError: {e}")
#Catching IndexError-
try:
    my_list = [1, 2, 3]
    element = my_list[5]  # Index out of bounds
except IndexError as e:
    print(f"Caught an IndexError: {e}")

# #Catching KeyError-
try:
    my_dict = {"name": "Alice", "age": 30}
    value = my_dict["address"]  # Key does not exist
except KeyError as e:
    print(f"Caught a KeyError: {e}")

# #Catching AttributeError:
try:
    my_string = "Hello, World"
    length = my_string.len()  # 'len' attribute does not exist
except AttributeError as e:
    print(f"Caught an AttributeError: {e}")

