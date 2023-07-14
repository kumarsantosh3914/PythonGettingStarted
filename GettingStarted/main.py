print("Hello World!")

# Arithmetic Operators

x = 9
y = 4

# Addition
print(x + y)

# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Division Float
print(x / y)

# Division Floor
print(x // y)

# Modulus - Returns the remainder when first operand is divided by the second
print(x % y)

# Power - returns first raised to power second
print(x ** y)


# ------------------------LOGICAL OPERATORS---------------------
a = True
b = False

# and - Logical AND: True if both the operands are true 
print(a and b)

# or - Logical OR: True if either of the operands is true 
print(a or b)

# not - Logical NOT: True if operand is false 
print(not x)


# -------------------------BITWISE OPERATORS----------------------------
a = 10
b = 4

# & - Bitwise AND
print(a & b)

# | - Bitwise OR
print(a | b)

# ~ - Bitwise NOT
print(~a)

# ^ - Bitwise XOR
print(a ^ b)

# >> - Bitwise right shift
print(a >> 2)

# << - Bitwise left shift
print(a << 2)


# ------------------------KEYWORDS------------------------------------

# yield

def generator():
    for i in range(6):
        yield i * i
g = generator()
for i in g:
    print(i)


# lambda - lambda is used to create an anonymous function (function with no name). It is an
# inline function that does not contain a return statement. It consists of an
# expression that is evaluated and returned.

a = lambda x: x * 2
for i in range(1, 6):
    print(a(i))


# async, await

# The async and await keywords are provided by the asyncio library in Python. They are used to write concurrent code in Python.

import asyncio
async def main():
    print('Hello')
    await async.sleep(1)
    print('World')

# To run the program, we use: 
async.run(main())

# finally
# finally is used with try....except block to close up resources or file streams.
# Using finally ensures that the block of code inside it gets executed even if there is an unhandled exception. 

def learnfinally():
    try:
        print("Inside try Block")  # No Exception raised
        return 1                   # before this, finally gets executed
    except Exception as e:
        print(e)
    finally:
        print("Inside Finally")
 
 
print(learnfinally())

# assert 
# assert is used for debugging purposes.
# While programming, sometimes we wish to know the internal state or check if our
# assumptions are true. assert helps us do this and find bugs more
# conveniently. assert is followed by a condition.
# If the condition is true, nothing happens. But if the condition is
# false, AssertionError is raised.

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    # Assertion to check that the length and width are positive
    assert length > 0 and width > 0, "Length and width"+ \
                "must be positive"
    # Calculation of the area
    area = length * width
    # Return statement
    return area
 
 
# Calling the function with positive inputs
area1 = calculate_rectangle_area(5, 6)
print("Area of rectangle with length 5 and width 6 is", area1)
 
# Calling the function with negative inputs
area2 = calculate_rectangle_area(-5, 6)
print("Area of rectangle with length -5 and width 6 is", area2)

# -----------------------BREAK AND CONTINUE-------------------------------

# CONTINUE
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# BREAK
for i in range(1, 11):
    if i == 5:
        break
    print(i)