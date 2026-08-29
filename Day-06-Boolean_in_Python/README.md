# Python Boolean Data Type

A **Boolean (`bool`)** is a built-in Python data type that represents one of two values:

```python
True
False
```

Boolean values are mainly used for **conditions, comparisons, and decision-making**.

---

## 1. Creating Boolean Values

```python
a = True
b = False

print(a)
print(b)

print(type(a))
print(type(b))
```

### Output

```text
True
False
<class 'bool'>
<class 'bool'>
```

---

## 2. Boolean from Comparisons

Comparison operators always return a Boolean value.

```python
a = 10
b = 5

print(a > b)
print(a < b)
print(a == b)
print(a != b)
```

### Output

```text
True
False
False
True
```

### Common Comparison Operators

| Operator | Meaning               | Example           |
| -------- | --------------------- | ----------------- |
| `==`     | Equal to              | `5 == 5` → `True` |
| `!=`     | Not equal to          | `5 != 3` → `True` |
| `>`      | Greater than          | `5 > 3` → `True`  |
| `<`      | Less than             | `3 < 5` → `True`  |
| `>=`     | Greater than or equal | `5 >= 5` → `True` |
| `<=`     | Less than or equal    | `3 <= 5` → `True` |

---

# 3. `bool()` Function

The `bool()` function converts a value into either `True` or `False`.

```python
print(bool(1))
print(bool(0))
print(bool("Python"))
print(bool(""))
```

### Output

```text
True
False
True
False
```

---

# 4. Truthy and Falsy Values

Python treats some values as **False** when used in a condition.

### Falsy Values

The important falsy values are:

```python
False
None
0
0.0
0j
""
[]
()
{}
set()
```

Everything else is generally **Truthy**.

### Example

```python
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))

print(bool(10))
print(bool("Python"))
print(bool([1, 2]))
```

### Output

```text
False
False
False
False
False
True
True
True
```

### Easy Rule ⭐

```text
Empty → False
Zero → False
None → False
Non-empty → True
Non-zero → True
```

---

# 5. Boolean with Integers

Zero is considered `False`.

Any non-zero number is considered `True`.

```python
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(100))
```

### Output

```text
False
True
True
True
```

---

# 6. `and` Operator

The `and` operator requires **both conditions to be True**.

```python
a = 10
b = 5

print(a > 5 and b < 10)
```

### Output

```text
True
```

Because:

```text
a > 5  → True
b < 10 → True

True and True → True
```

### Truth Table

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

---

# 7. `or` Operator

The `or` operator returns `True` if **at least one condition is True**.

```python
a = 10
b = 5

print(a > 20 or b < 10)
```

### Output

```text
True
```

Because:

```text
a > 20 → False
b < 10 → True

False or True → True
```

### Truth Table

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

---

# 8. `not` Operator

`not` reverses a Boolean value.

```python
print(not True)
print(not False)
```

### Output

```text
False
True
```

Example:

```python
a = 0

print(not a)
```

### Output

```text
True
```

Because:

```text
0 → False
not False → True
```

---

# 9. Combining Boolean Operators

We can combine `and`, `or`, and `not`.

```python
age = 20
has_id = True

print(age >= 18 and has_id)
```

### Output

```text
True
```

Both conditions are True.

---

# 10. Boolean in `if` Statements

Boolean values are heavily used in decision-making.

```python
age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

### Output

```text
Eligible to vote
```

The expression:

```python
age >= 18
```

produces:

```python
True
```

So the `if` block executes.

---

# 11. Boolean with Strings

```python
name = "Bhoomika"

if name:
    print("Name is available")
```

### Output

```text
Name is available
```

An empty string is falsy:

```python
name = ""

if name:
    print("Name is available")
else:
    print("Name is empty")
```

### Output

```text
Name is empty
```

---

# 12. Equality Operator `==`

`==` checks whether two values are equal.

```python
a = 10
b = 10

print(a == b)
```

### Output

```text
True
```

---

# 13. Not Equal Operator `!=`

`!=` checks whether two values are different.

```python
a = 10
b = 5

print(a != b)
```

### Output

```text
True
```

---

# 14. Identity Operator `is`

`is` checks whether two variables refer to the **same object**.

```python
a = None

print(a is None)
```

### Output

```text
True
```

### Important ⭐

Do not normally use `is` to compare values.

Use:

```python
==
```

for value comparison.

Use:

```python
is
```

for object identity, especially common cases like:

```python
x is None
```

---

# 15. Membership Operator `in`

`in` checks whether an element exists inside a sequence such as a list, tuple, set, or string.

```python
numbers = [10, 20, 30]

print(20 in numbers)
print(50 in numbers)
```

### Output

```text
True
False
```

---

# 16. `not in`

`not in` checks whether an element does **not** exist.

```python
numbers = [10, 20, 30]

print(50 not in numbers)
print(20 not in numbers)
```

### Output

```text
True
False
```

---

# 17. Boolean with Lists

```python
numbers = []

print(bool(numbers))
```

### Output

```text
False
```

Non-empty list:

```python
numbers = [1, 2, 3]

print(bool(numbers))
```

### Output

```text
True
```

This is useful in conditions:

```python
numbers = [1, 2, 3]

if numbers:
    print("List is not empty")
```

---

# 18. Boolean Expressions

An expression that produces `True` or `False` is called a **Boolean expression**.

```python
x = 10
y = 20

result = x < y

print(result)
print(type(result))
```

### Output

```text
True
<class 'bool'>
```

---

# 19. Multiple Conditions

```python
age = 21
marks = 80

if age >= 18 and marks >= 40:
    print("Eligible")
else:
    print("Not eligible")
```

### Output

```text
Eligible
```

Both conditions must be satisfied.

---

# 20. Operator Precedence

When multiple Boolean operators are used, Python follows an order.

The important order is:

```text
1. not
2. and
3. or
```

Example:

```python
print(True or False and False)
```

Python evaluates:

```text
False and False → False
True or False   → True
```

### Output

```text
True
```

Use parentheses when you want to make the logic clear:

```python
print((True or False) and False)
```

### Output

```text
False
```

---

# 21. Boolean Conversion Examples

```python
values = [0, 1, "", "Python", [], [1, 2], None]

for value in values:
    print(value, "→", bool(value))
```

### Output

```text
0 → False
1 → True
 → False
Python → True
[] → False
[1, 2] → True
None → False
```

---

# 22. Important Difference: `=` vs `==`

This is very important in Python.

### `=`

Used for **assignment**.

```python
x = 10
```

Means:

```text
Store 10 in x
```

### `==`

Used for **comparison**.

```python
x == 10
```

Means:

```text
Is x equal to 10?
```

It returns:

```python
True
```

or

```python
False
```

---

# 23. Practical Example

```python
username = "Bhoomika"
password = "1234"

if username == "Bhoomika" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")
```

### Output

```text
Login successful
```

This shows how Boolean expressions are used in real programs.

---

# 24. Quick Revision ⭐

```text
Boolean → True or False

bool() → Converts a value to Boolean

0 → False
Non-zero → True

"" → False
Non-empty string → True

[] → False
Non-empty list → True

() → False
Non-empty tuple → True

{} → False
Non-empty dictionary → True

None → False
```

### Boolean Operators

```text
and → Both conditions must be True
or  → At least one condition must be True
not → Reverses the result
```

### Comparison Operators

```text
== → Equal
!= → Not equal
>  → Greater than
<  → Less than
>= → Greater than or equal
<= → Less than or equal
```

### Other Useful Operators

```text
is     → Same object?
is not → Different objects?
in     → Element exists?
not in → Element doesn't exist?
```

---

# 25. Practice Questions

Try solving these yourself:

### Q1

```python
print(bool(0))
print(bool(10))
```

### Q2

```python
print(10 > 5 and 3 < 2)
```

### Q3

```python
print(10 > 5 or 3 < 2)
```

### Q4

```python
print(not False)
```

### Q5

```python
numbers = [10, 20, 30]
print(20 in numbers)
```

### Q6

```python
name = ""

if name:
    print("Hello")
else:
    print("No name")
```

### Q7

What is the difference between:

```python
=
==
```

---

## ⭐ One-Line Definition

> **Boolean is a Python data type that represents either `True` or `False` and is mainly used for comparisons, conditions, and decision-making.**
