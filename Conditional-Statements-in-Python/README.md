# Conditional Statements in Python

Conditional statements are used to **control the flow of a program** based on whether a condition is `True` or `False`.

Python mainly provides:

1. `if`
2. `if-else`
3. `if-elif-else`
4. Nested `if`
5. Conditional Expression (Ternary Operator)
6. `match-case`

---

# 1. if Statement

The `if` statement executes a block of code **only when the condition is True**.

### Syntax

```python
if condition:
    # code to execute
```

### Example

```python
age = 20

if age >= 18:
    print("Eligible to vote.")
```

Output:

```text
Eligible to vote.
```

### How it works

```text
age >= 18
   ↓
 True
   ↓
Execute print()
```

If the condition is `False`, the code inside the `if` block is skipped.

---

# 2. Short-Hand if

If there is only one statement inside the `if`, it can be written in one line.

```python
age = 20

if age >= 18: print("Eligible to vote.")
```

Output:

```text
Eligible to vote.
```

This is useful for very simple conditions, but normal multi-line `if` statements are usually easier to read.

---

# 3. if-else Statement

`if-else` is used when there are **two possible outcomes**.

* If the condition is `True` → execute `if`
* If the condition is `False` → execute `else`

### Syntax

```python
if condition:
    # if condition is True
else:
    # if condition is False
```

### Example

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```text
Minor
```

### Flow

```text
        Condition
        /       \
     True       False
      ↓           ↓
     if          else
```

---

# 4. if-elif-else Statement

`elif` means **else if**.

It is used when we need to check **multiple conditions**.

### Syntax

```python
if condition1:
    # code
elif condition2:
    # code
elif condition3:
    # code
else:
    # code
```

Python checks conditions **from top to bottom**.

As soon as it finds a `True` condition, that block executes and the remaining conditions are skipped.

### Example

```python
age = 25

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 35:
    print("Young Adult")
else:
    print("Adult")
```

Output:

```text
Young Adult
```

### Important

For:

```python
age = 25
```

Python checks:

```text
25 <= 12  → False
25 <= 19  → False
25 <= 35  → True
```

So it executes:

```python
print("Young Adult")
```

---

# 5. Nested if

A **nested if** means putting one `if` statement inside another `if` statement.

It is useful when one condition depends on another condition.

### Example

```python
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount")
    else:
        print("20% senior discount")
else:
    print("Not eligible for senior discount")
```

Output:

```text
30% senior discount
```

### How it works

First:

```python
age >= 60
```

is checked.

If it is `True`, Python checks:

```python
is_member
```

So:

```text
age >= 60
     ↓
   True
     ↓
is_member?
  ↓       ↓
True    False
 ↓        ↓
30%      20%
```

---

# 6. Conditional Expression (Ternary Operator)

A **ternary operator**, also called a **conditional expression**, is a short way to write a simple `if-else` statement in one line.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Example

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output:

```text
Adult
```

### Normal if-else

```python
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

### Ternary version

```python
status = "Adult" if age >= 18 else "Minor"
```

Both produce the same result.

---

# 7. Ternary Example: Even or Odd

```python
n = 5

result = "Even" if n % 2 == 0 else "Odd"

print(result)
```

Output:

```text
Odd
```

### Explanation

```python
n % 2 == 0
```

checks whether the number is divisible by 2.

For `5`:

```text
5 % 2 = 1
```

So the condition is `False`.

Therefore:

```text
"Odd"
```

is selected.

---

# 8. Nested Ternary Operator

A ternary expression can be nested to check multiple conditions.

```python
num = -5

result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"

print(result)
```

Output:

```text
Negative
```

### Logic

```text
num > 0?
 ↓
False
 ↓
num < 0?
 ↓
True
 ↓
"Negative"
```

⚠️ Nested ternary expressions can become difficult to read. For complex logic, use normal `if-elif-else`.

---

# 9. Ternary with print()

A ternary expression can be directly used inside `print()`.

```python
a = 10
b = 20

print("a is greater" if a > b else "b is greater")
```

Output:

```text
b is greater
```

---

# 10. Match-Case Statement

`match-case` is used to compare a value against multiple patterns.

It is similar to the `switch-case` statement found in languages such as C, C++ and Java.

### Syntax

```python
match value:
    case pattern1:
        # code
    case pattern2:
        # code
    case _:
        # default case
```

### Example

```python
number = 2

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other")
```

Output:

```text
Two
```

---

# 11. Multiple Patterns in match-case

The `|` operator can match multiple patterns.

```python
number = 3

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other")
```

Output:

```text
Two or Three
```

Here:

```python
case 2 | 3:
```

means:

```text
2 OR 3
```

---

# 12. Default Case `_`

In `match-case`, `_` works like a default case.

```python
number = 10

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Something else")
```

Output:

```text
Something else
```

If none of the previous cases match, `_` is executed.

---

# 13. Comparison Operators in Conditions

Conditional statements commonly use comparison operators.

| Operator | Meaning               | Example  |
| -------- | --------------------- | -------- |
| `==`     | Equal to              | `a == b` |
| `!=`     | Not equal to          | `a != b` |
| `>`      | Greater than          | `a > b`  |
| `<`      | Less than             | `a < b`  |
| `>=`     | Greater than or equal | `a >= b` |
| `<=`     | Less than or equal    | `a <= b` |

Example:

```python
a = 10
b = 5

if a > b:
    print("a is greater")
```

Output:

```text
a is greater
```

---

# 14. Logical Operators in Conditions

Logical operators allow us to combine conditions.

### `and`

Returns `True` when **both conditions are True**.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
```

### `or`

Returns `True` when **at least one condition is True**.

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

### `not`

Reverses a Boolean value.

```python
is_raining = False

if not is_raining:
    print("Go outside")
```

---

# 15. Truthy and Falsy Values in Conditions

Python automatically treats values as either **truthy** or **falsy** when used in a condition.

### Truthy examples

```python
if 1:
    print("Truthy")

if -5:
    print("Truthy")

if "Hello":
    print("Truthy")

if [1, 2]:
    print("Truthy")
```

### Falsy examples

```python
if 0:
    print("This will not execute")

if "":
    print("This will not execute")

if []:
    print("This will not execute")

if None:
    print("This will not execute")
```

### Main falsy values to remember

```text
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

Most other values are truthy.

---

# 16. `if` with a Number

This is useful to understand truthy/falsy values.

```python
num = 10

if num:
    print("Truthy")
```

Output:

```text
Truthy
```

Because:

```text
10 → non-zero → Truthy
```

But:

```python
num = 0

if num:
    print("Truthy")
else:
    print("Falsy")
```

Output:

```text
Falsy
```

Because:

```text
0 → Falsy
```

---

# 17. `if` with Modulo

The `%` operator returns the remainder.

This can be used with conditions to check odd/even numbers.

```python
num = 7

if num % 2:
    print("Odd")
else:
    print("Even")
```

Output:

```text
Odd
```

Why?

```text
7 % 2 = 1
```

`1` is truthy.

For an even number:

```python
num = 8

if num % 2:
    print("Odd")
else:
    print("Even")
```

Output:

```text
Even
```

Because:

```text
8 % 2 = 0
```

`0` is falsy.

---

# 18. Important Difference: `=` vs `==`

This is very important.

### `=`

Used for **assignment**.

```python
age = 20
```

Means:

> Store `20` in `age`.

### `==`

Used for **comparison**.

```python
age == 20
```

Means:

> Is `age` equal to `20`?

Example:

```python
age = 20

if age == 20:
    print("Age is 20")
```

Output:

```text
Age is 20
```

---

# 19. Combining Conditions

We can combine multiple conditions.

```python
age = 20
marks = 80

if age >= 18 and marks >= 40:
    print("Eligible")
else:
    print("Not Eligible")
```

Both conditions must be true because we used `and`.

---

# 20. `if-elif-else` vs Nested `if`

### `if-elif-else`

Use when checking **different alternatives**:

```python
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")
```

### Nested `if`

Use when one condition depends on another:

```python
if age >= 18:
    if has_id:
        print("Allowed")
```

---

# 21. Important Rules for Python Conditions

### Indentation is required

Correct:

```python
if age >= 18:
    print("Adult")
```

Incorrect:

```python
if age >= 18:
print("Adult")
```

Python uses indentation to determine which statements belong to a block.

### Colon `:` is required

```python
if condition:
    print("Hello")
```

The colon tells Python that a block of code follows.

---

# 22. Complete Example

```python
marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
```

Output:

```text
Grade: A
```

---

# ⭐ Quick Revision

```text
Conditional Statements
        ↓
 ┌──────┼─────────────┐
 ↓      ↓             ↓
if    if-else    if-elif-else
        ↓
    Nested if
        ↓
    Ternary
        ↓
   match-case
```

### `if`

```python
if condition:
    statement
```

### `if-else`

```python
if condition:
    statement
else:
    statement
```

### `if-elif-else`

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

### Ternary

```python
value_if_true if condition else value_if_false
```

### Match-case

```python
match value:
    case pattern:
        statement
    case _:
        statement
```

---

# ⭐ Most Important Things to Remember

```text
if          → One condition
if-else     → Two possible paths
elif        → Multiple conditions
nested if   → Condition inside another condition
ternary     → Short one-line if-else
match-case  → Match a value against patterns
```

And always remember:

```text
=   → Assignment
==  → Comparison

and → Both must be True
or  → At least one must be True
not → Reverses True/False

0, "", [], {}, None → Falsy
Most non-empty/non-zero values → Truthy
```

# One-Line Definition

> **Conditional statements in Python control the flow of execution by executing different blocks of code depending on whether specified conditions are True or False.**
