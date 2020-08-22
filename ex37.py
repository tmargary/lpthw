################    as

# instead of

f = open('test.txt')
f.read()
f.close

# you can write

with open('test.txt') as f:
    f.read()
    f.close

x = "hello"

################    assert

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
# assert x == "goodbye"

################    break

# End the loop if i is larger than 3:

for i in range(9):
    if i > 3:
        break
    print(i)

################    class

# Create a class named "Person":

class Person:
    name = "John"
    age = 36

################    continue

# Skip the iteration if the variable i is 3, but continue with the next iteration:

for i in range(5):
    if i == 3:
        continue
    print(i)

################    def

# Create and execute a function:

def my_function():
      print("Hello from a function")

my_function()

################    del

# Delete an object:

class MyClass:
    name = "John"

del MyClass

# print(MyClass) prints an error that MyClass doesn't exost

################    elif

# Used in conditional statements, same as else if

################    else

# Used in conditional statements

################    except

# If the statement raises an error print "Something went wrong":

try:
    x > 3
except:
    print("Something went wrong")

################    False

# Boolean value, result of comparison operations

################    finally

# The finally block will always be executed, no matter if the try block raises an error or not:

try:
    x > 3
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The try...except block is finished")

################    for

# To create a for loop

################    from

# Import only the time section from the datetime module, and print the time as if it was 15:00:

from datetime import time

x = time(hour=15)

print(x)

################    global

# Declare a global variable inside a function, and use it outside the function:

#create a function:
def myfunction():
    global x
    x = "hello"

#execute the function:
myfunction()

#x should now be global, and accessible in the global scope.
print(x)

################    if

# To make a conditional statement

################    import

# To import a module

################    in

# To check if a value is present in a list, tuple, etc.

################    is

# Check if two objects are the same object:

x = ["apple", "banana", "cherry"]

y = x

print(x is y)

################    lambda

# Create a function that adds 10 to any number you send:

x = lambda a : a + 10

print(x(5))

################    None

# Represents a null value

################    nonlocal

# To declare a non-local variable

################    not

# Return True if the statement is not True:

x = False

print(not x)

################    or

# A logical operator

################    pass

# A null statement, a statement that will do nothing

################    raise

# Raise a TypeError if x is not an integer:

x = 12

if not type(x) is int:
    raise TypeError("Only integers are allowed")

################    return

# To exit a function and return a value

################    try

# To make a try...except statement

################    while

# To create a while loop

################    with

# Used to simplify exception handling

################    yield

# To end a function, returns a generator

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

################    ##

print("abc\vabc")
