# Variables and Python Basics - Examples

# 1. Variables

age = 20
name = "Bhoomi"

print(age)
print(name)

# 2. Different Values

number = 10
price = 99.5
message = "Hello Python"
is_student = True

print(number)
print(price)
print(message)
print(is_student)

# 3. Reassignment

x = 10
print("Before reassignment:", x)

x = 20
print("After reassignment:", x)

# 4. Object References

a = 10
b = a

print("a:", a)
print("b:", b)

# 5. Swapping Two Variables

first = 10
second = 20

first, second = second, first

print("First:", first)
print("Second:", second)

# 6. Counting Characters

text = "Python"

print("Number of characters:", len(text))

# 7. Counting Characters Including Space

text = "Hello World"

print("Number of characters:", len(text))

# 8. Operators

a = 5
b = 2

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# 9. Bitwise NOT

a = 5

print("Bitwise NOT of 5:", ~a)

also remeber for bitwise opr formula ~a = -(a + 1)

# 10. Deleting a Variable

value = 100
print("Before deleting:", value)

del value

# value can no longer be used here
