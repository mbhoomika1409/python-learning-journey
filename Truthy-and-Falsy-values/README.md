# Truthy and Falsy Values in Python

In Python, **every value has a Boolean meaning** when it is used in a condition.

* **Truthy** → A value that behaves like `True`.
* **Falsy** → A value that behaves like `False`.

Python automatically checks the truthiness of a value in conditions such as `if` and `while`.

---

## 1. Basic Example

```python
if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")
```

### Output

```text
1 is truthy
0 is falsy
```

Why?

```text
1 → Truthy
0 → Falsy
```

---

# 2. Truthy Values

A value is generally **truthy** when it is:

* A non-zero number
* A non-empty string
* A non-empty list, tuple, set, or dictionary
* `True`

### Examples

```python
if 7:
    print("7 is truthy")

if -4:
    print("-4 is truthy")

if "Hello":
    print("String is truthy")

if [1, 2]:
    print("List is truthy")
```

### Output

```text
7 is truthy
-4 is truthy
String is truthy
List is truthy
```

---

# 3. Falsy Values

The most important falsy values in Python are:

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
range(0)
```

These values evaluate to `False` in a Boolean context.

---

# 4. Numbers

### Zero → Falsy

```python
print(bool(0))
print(bool(0.0))
print(bool(0j))
```

### Output

```text
False
False
False
```

### Non-zero → Truthy

```python
print(bool(10))
print(bool(-5))
print(bool(3.14))
```

### Output

```text
True
True
True
```

### ⭐ Easy Rule

```text
0 → Falsy
Any non-zero number → Truthy
```

---

# 5. Strings

An **empty string** is falsy.

```python
print(bool(""))
```

Output:

```text
False
```

A **non-empty string** is truthy.

```python
print(bool("Python"))
print(bool("Hello"))
```

Output:

```text
True
True
```

### ⭐ Remember

```text
"" → Falsy
"Python" → Truthy
```

---

# 6. Lists

An empty list is falsy:

```python
print(bool([]))
```

Output:

```text
False
```

A non-empty list is truthy:

```python
print(bool([1, 2, 3]))
```

Output:

```text
True
```

So:

```text
[] → Falsy
[1, 2, 3] → Truthy
```

---

# 7. Tuples

An empty tuple is falsy:

```python
print(bool(()))
```

Output:

```text
False
```

A non-empty tuple is truthy:

```python
print(bool((1, 2)))
```

Output:

```text
True
```

---

# 8. Dictionaries

An empty dictionary is falsy:

```python
print(bool({}))
```

Output:

```text
False
```

A non-empty dictionary is truthy:

```python
print(bool({"name": "Bhoomika"}))
```

Output:

```text
True
```

---

# 9. `None`

`None` represents the absence of a value.

```python
print(bool(None))
```

Output:

```text
False
```

Example:

```python
name = None

if name:
    print("Name exists")
else:
    print("No name")
```

Output:

```text
No name
```

---

# 10. `True` and `False`

```python
print(bool(True))
print(bool(False))
```

Output:

```text
True
False
```

---

# 11. Using Truthy/Falsy Directly in `if`

We don't always need to write:

```python
if bool(number):
```

Python automatically checks the value.

Instead, we can simply write:

```python
number = 7

if number:
    print("Number exists")
```

Since `7` is truthy, the condition executes.

---

# 12. Important Example: Odd and Even

Truthy/falsy values can make conditions shorter.

```python
num1 = 7
num2 = 4

if num1 % 2:
    print(num1, "is odd")
else:
    print(num1, "is even")

if num2 % 2:
    print(num2, "is odd")
else:
    print(num2, "is even")
```

### Output

```text
7 is odd
4 is even
```

### Why?

For `7`:

```text
7 % 2 = 1
```

`1` is non-zero → **Truthy**

Therefore:

```python
if 1:
```

runs.

For `4`:

```text
4 % 2 = 0
```

`0` is → **Falsy**

Therefore:

```python
if 0:
```

does not run, so the `else` block executes.

### ⭐ Important Pattern

```text
number % 2

1 → Truthy → Odd
0 → Falsy  → Even
```

---

# 13. Using `not`

`not` reverses the truthiness.

```python
if not 0:
    print("0 is falsy")

if not []:
    print("Empty list is falsy")
```

### Output

```text
0 is falsy
Empty list is falsy
```

Why?

```text
0 → False
not False → True
```

and:

```text
[] → False
not False → True
```

---

# 14. `bool()` Function

The `bool()` function explicitly converts a value into `True` or `False`.

### Syntax

```python
bool(value)
```

Example:

```python
print(bool(7))
print(bool(0))
print(bool([1, 2, 3]))
print(bool([]))
print(bool(None))
```

### Output

```text
True
False
True
False
False
```

---

# 15. Truthy vs Falsy Table ⭐

| Value      | Boolean | Type   |
| ---------- | ------- | ------ |
| `True`     | `True`  | Truthy |
| `False`    | `False` | Falsy  |
| `1`        | `True`  | Truthy |
| `-5`       | `True`  | Truthy |
| `0`        | `False` | Falsy  |
| `"Hello"`  | `True`  | Truthy |
| `""`       | `False` | Falsy  |
| `[1, 2]`   | `True`  | Truthy |
| `[]`       | `False` | Falsy  |
| `(1, 2)`   | `True`  | Truthy |
| `()`       | `False` | Falsy  |
| `{"a": 1}` | `True`  | Truthy |
| `{}`       | `False` | Falsy  |
| `None`     | `False` | Falsy  |

---

# 16. Real-World Example

Suppose we want to check whether a username was entered.

```python
username = "Bhoomika"

if username:
    print("Username entered")
else:
    print("Username is empty")
```

Output:

```text
Username entered
```

If:

```python
username = ""
```

then:

```text
Username is empty
```

Because:

```text
"Bhoomika" → Truthy
"" → Falsy
```

---

# 17. Truthy/Falsy with `while`

Truthy and falsy values can also be used in `while` loops.

```python
number = 3

while number:
    print(number)
    number -= 1
```

### Output

```text
3
2
1
```

When `number` becomes `0`, it becomes falsy and the loop stops.

---

# 18. Most Important Rules ⭐⭐⭐

Remember these rules:

```text
ZERO → Falsy
EMPTY → Falsy
NONE → Falsy
FALSE → Falsy

NON-ZERO → Truthy
NON-EMPTY → Truthy
TRUE → Truthy
```

### Examples

```text
0       → False
10      → True

""      → False
"Hello" → True

[]      → False
[1, 2]  → True

()      → False
(1, 2)  → True

{}      → False
{"a":1} → True

None    → False
True    → True
```

---

# 19. Quick Revision

```python
# Numbers
bool(0)      # False
bool(10)     # True

# Strings
bool("")     # False
bool("Hi")   # True

# Lists
bool([])     # False
bool([1])    # True

# Tuples
bool(())     # False
bool((1,))   # True

# Dictionary
bool({})     # False
bool({"a":1})# True

# None
bool(None)   # False
```

### ⭐ One-Line Definition

> **Truthy values are values that evaluate to `True` in a Boolean context, while falsy values evaluate to `False`.**
