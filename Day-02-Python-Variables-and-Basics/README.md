# Python Variables and Basics

## 📌 Topics Covered

1. Variables in Python
2. Rules for Naming Variables
3. Tokens and Character Sets
4. Keywords
5. Identifiers
6. Literals

   * Numerical Literals
   * String Literals
   * Boolean Literals
   * Collection Literals
7. Operators
8. Punctuators
9. Assigning Values to Variables
10. Different Values Assigned to Variables
11. Object References
12. Variable Reassignment
13. Deleting a Variable
14. Swapping Two Variables
15. Counting Characters in a String

---

# 1. Variables in Python

A **variable** is a name used to store or refer to a value in Python.

```python
age = 20
name = "Bhoomi"
```

Here:

* `age` → variable
* `20` → value
* `name` → variable
* `"Bhoomi"` → value

### Easy Meaning

> **Variable = Name that refers to a value**

---

# 2. Rules for Naming Variables

Python variable names must follow these rules:

### ✅ Valid

```python
age = 20
student_name = "Bhoomi"
marks2 = 90
_total = 100
```

### ❌ Invalid

```python
2age = 20
student-name = "Bhoomi"
student name = "Bhoomi"
for = 10
```

### Important Rules

1. A variable name can contain letters.
2. It can contain numbers.
3. It can contain `_`.
4. It cannot start with a number.
5. Spaces are not allowed.
6. Special characters such as `@`, `#`, `$`, `-` are not allowed.
7. Python keywords cannot be used as variable names.
8. Variable names are case-sensitive.

Example:

```python
age = 20
Age = 30
```

`age` and `Age` are different variables.

---

# 3. Tokens and Character Set

## Character Set

A **character set** is the collection of characters that can be used in Python programs.

Examples:

* Alphabets: `A-Z`, `a-z`
* Digits: `0-9`
* Special characters: `+`, `-`, `*`, `/`, `_`, etc.
* Whitespace characters

## Tokens

A **token** is the smallest meaningful unit of a Python program.

Main types of tokens:

1. Keywords
2. Identifiers
3. Literals
4. Operators
5. Punctuators

Example:

```python
age = 20
```

Tokens are:

```text
age
=
20
```

---

# 4. Keywords

**Keywords are reserved words in Python that have a predefined meaning.**

Examples:

```text
if
else
for
while
def
class
return
True
False
None
```

### Easy Meaning

> **Keyword = Python's reserved word**

Keywords cannot normally be used as variable names.

```python
for = 10
```

❌ Invalid

---

# 5. Identifiers

An **identifier** is a name given by the programmer to variables, functions, classes, etc.

Examples:

```python
age
student_name
total
calculate_sum
```

### Easy Meaning

> **Identifier = Name given by the programmer**

Example:

```python
age = 20
```

Here `age` is an identifier.

---

# 6. Literals

A **literal** is a fixed value written directly in a Python program.

## A. Numerical Literals

Numbers such as:

```python
10
25
3.14
-5
```

Examples:

```python
age = 20
price = 99.5
```

---

## B. String Literals

Text written inside quotes.

```python
"Hello"
'Python'
"Bhoomi"
```

Example:

```python
name = "Bhoomi"
```

---

## C. Boolean Literals

Boolean values represent:

```python
True
False
```

Example:

```python
is_student = True
```

---

## D. Collection Literals

Collections can store multiple values.

### List

```python
numbers = [1, 2, 3]
```

### Tuple

```python
numbers = (1, 2, 3)
```

### Set

```python
numbers = {1, 2, 3}
```

### Dictionary

```python
student = {"name": "Bhoomi", "age": 20}
```

---

# 7. Operators

Operators are symbols used to perform operations.

The values on which operations are performed are called **operands**.

Example:

```python
a = 5
b = 2

print(a + b)
```

Here:

* `+` → operator
* `a` and `b` → operands

## Common Operators

### Arithmetic Operators

```text
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus
//  Floor Division
**  Power
```

### Comparison Operators

```text
==  Equal
!=  Not Equal
>   Greater than
<   Less than
>=  Greater than or Equal
<=  Less than or Equal
```

### Logical Operators

```text
and
or
not
```

### Bitwise Operators

```text
&   AND
|   OR
^   XOR
~   NOT
```

Example:

```python
a = 5

print(~a)
```

Output:

```text
-6
```

### Why `~5` is `-6`

Easy formula:

```text
~n = -(n + 1)
```

Therefore:

```text
~5 = -(5 + 1)
   = -6
```

---

# 8. Punctuators

**Punctuators are symbols used to organize and structure Python code.**

Examples:

```text
( )
[ ]
{ }
:
,
.
;
@
```

Example:

```python
numbers = [1, 2, 3]
```

Here:

* `[` and `]` → punctuators
* `,` → punctuator

---

# 9. Assigning a Value to a Variable

The `=` operator is used to assign a value to a variable.

```python
age = 20
name = "Bhoomi"
```

Here:

```text
age → variable
=   → assignment operator
20  → value
```

### Easy Meaning

> `=` means **assign this value to this variable**.

---

# 10. Different Values Assigned to Variables

Python variables can store different types of values.

```python
age = 20
name = "Bhoomi"
height = 5.5
is_student = True
```

The same variable can also be reassigned to a different type of value:

```python
x = 10
x = "Hello"
```

Python allows this because it is **dynamically typed**.

---

# 11. Object References

In Python, a variable is a **reference to an object** rather than a box that physically contains the value.

Example:

```python
x = 10
```

Here:

```text
x ─────> 10
```

The variable `x` refers to the integer object `10`.

Another example:

```python
a = 10
b = a
```

Both variables can refer to the same object:

```text
a ──┐
    ├──> 10
b ──┘
```

---

# 12. Variable Reassignment

A variable can be assigned a new value.

```python
x = 10
print(x)

x = 20
print(x)
```

Output:

```text
10
20
```

The variable `x` now refers to the new value `20`.

### Easy Meaning

> **Reassignment = Giving a new value to an existing variable**

---

# 13. Deleting a Variable

The `del` keyword can be used to delete a variable.

```python
x = 10

del x
```

After deleting it, trying to use `x` will cause an error.

```python
print(x)
```

This produces a `NameError` because `x` no longer exists as a defined variable.

---

# 14. Swapping Two Variables

Python allows two variables to be swapped easily.

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

### Easy Meaning

Before:

```text
a = 10
b = 20
```

After:

```text
a = 20
b = 10
```

Python allows this without needing a temporary variable.

---

# 15. Counting Characters in a String

The `len()` function is used to find the number of characters in a string.

Example:

```python
text = "Python"

print(len(text))
```

Output:

```text
6
```

Because:

```text
P y t h o n
1 2 3 4 5 6
```

Spaces are also counted.

Example:

```python
text = "Hello World"

print(len(text))
```

Output:

```text
11
```

---

# 🧠 Quick Revision

| Topic            | Easy Meaning                 |
| ---------------- | ---------------------------- |
| Variable         | Name referring to a value    |
| Keyword          | Python's reserved word       |
| Identifier       | Programmer-given name        |
| Literal          | Fixed value                  |
| Operator         | Performs an operation        |
| Operand          | Value used in an operation   |
| Punctuator       | Symbol that structures code  |
| Assignment       | Giving a value to a variable |
| Reassignment     | Giving a new value           |
| Object Reference | Variable refers to an object |
| `del`            | Deletes a variable           |
| `len()`          | Counts characters            |

---

# 🎯 Important Memory Tricks

```text
Keyword     → Python's word
Identifier  → Programmer's name
Variable    → Name referring to data
Literal     → Actual/fixed value
Operator    → Performs operation
Operand     → Gets operated on
Punctuator  → Structures code
```

### Most Important

```text
Mutable   → Changeable
Immutable → Unchangeable

Valid     → Python accepts it
Invalid   → Python rejects it
```

---

# 📌 Conclusion

Python variables are names that refer to objects. Python provides different types of tokens such as keywords, identifiers, literals, operators, and punctuators to build programs. Understanding these basic concepts is important before learning more advanced Python topics.
