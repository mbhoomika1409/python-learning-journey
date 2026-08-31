PYTHON FUNCTIONS

A function is a reusable block of code that performs a specific task.

Functions help organize programs into smaller sections and allow us to reuse the same logic whenever needed by calling the function.


WHY DO WE USE FUNCTIONS?

1. Code Reusability
   - Write code once and use it multiple times.

2. Reduce Code Repetition
   - Avoid writing the same code again and again.

3. Easy to Understand
   - Break a large program into smaller, meaningful parts.

4. Easy Debugging
   - Errors can be found and fixed more easily.

5. Better Program Organization
   - Keeps the program clean and structured.


1. DEFINING A FUNCTION

We use the 'def' keyword to define a function.

SYNTAX:

def function_name():
    # statements


EXAMPLE:

def fun():
    print("Welcome to GFG")

Here:

def        -> Keyword used to define a function
fun        -> Function name
()         -> Parentheses used for parameters
:          -> Starts the function body
print()    -> Statement executed when the function is called


IMPORTANT:

Defining a function does NOT execute the function.

The function executes only when we CALL it.


2. CALLING A FUNCTION

After creating a function, we call it using the function name followed by parentheses.

EXAMPLE:

def fun():
    print("Welcome to GFG")

fun()

OUTPUT:

Welcome to GFG


HOW IT WORKS:

Function Definition
        ↓
def fun():
        ↓
Function is created
        ↓
fun()
        ↓
Function executes
        ↓
Welcome to GFG


3. FUNCTION WITH PARAMETERS

A function can accept values called parameters.

EXAMPLE:

def greet(name):
    print("Hello", name)

greet("Bhoomika")

OUTPUT:

Hello Bhoomika

Here:

name -> Parameter
"Bhoomika" -> Argument


4. PARAMETER VS ARGUMENT

Example:

def greet(name):
    print(name)

greet("Bhoomika")

name -> Parameter
"Bhoomika" -> Argument

Parameter:
A variable written inside the function definition.

Argument:
The actual value passed to the function when calling it.


5. MULTIPLE PARAMETERS

A function can have more than one parameter.

EXAMPLE:

def add(a, b):
    print(a + b)

add(10, 20)

OUTPUT:

30

Here:

a = 10
b = 20


6. RETURN STATEMENT

The 'return' statement is used to send a value back from a function.

EXAMPLE:

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

OUTPUT:

30


PRINT VS RETURN

print():
- Displays the value on the screen.

return:
- Sends the value back to the place where the function was called.
- The returned value can be stored in a variable or used in another operation.


7. FUNCTION WITHOUT RETURN

EXAMPLE:

def add(a, b):
    print(a + b)

add(10, 20)

OUTPUT:

30


8. FUNCTION WITH RETURN

EXAMPLE:

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

OUTPUT:

30

The returned value can be stored and used later.


9. IMPORTANT EXAMPLE

def square(n):
    return n * n

x = square(5)

print(x)

OUTPUT:

25


FLOW:

square(5)
   ↓
n = 5
   ↓
5 × 5
   ↓
25
   ↓
x = 25


BASIC FUNCTION STRUCTURE

def function_name(parameters):
    # statements
    return value

function_name(arguments)


QUICK REVISION

Function:
A reusable block of code that performs a specific task.

def:
Keyword used to define a function.

Calling:
Executing a function.

Parameter:
Variable inside the function definition.

Argument:
Actual value passed to a function.

return:
Sends a value back from the function.

print():
Displays output.


MOST IMPORTANT CONCEPT:

DEFINE → CALL → EXECUTE → RETURN (if needed)
