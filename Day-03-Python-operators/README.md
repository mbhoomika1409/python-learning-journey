# Python Operators (Beginner-Friendly Notes)

## 1. What are Operators?

Think of operators like **verbs** in a sentence — they tell Python what action to perform on some values.

The values operators work on are called **operands**.

```python
a = 10
b = 3
print(a + b)   # here '+' is the operator, 'a' and 'b' are operands
```

Analogy: if `a` and `b` are two numbers you're holding in your hands, the operator (`+`, `-`, etc.) is the *action* you perform with them — add them, compare them, combine them.

Without operators, a programming language can only *store* values — operators let it actually *do* something with them.

---

## 2. Types of Operators (Overview)

Python groups operators by what kind of job they do:

| Type | What it does | Symbols/Keywords |
|---|---|---|
| **Arithmetic** | Math operations (add, subtract, etc.) | `+ - * / // % **` |
| **Relational (Comparison)** | Compares two values, gives True/False | `== != > < >= <=` |
| **Logical** | Combines True/False conditions | `and or not` |
| **Bitwise** | Works on binary (bit-level) representation of numbers | `& \| ^ ~ << >>` |
| **Assignment** | Assigns/updates values in a variable | `= += -= *= /= //= %= **= &= \|= ^= >>= <<=` |
| **Ternary (Conditional)** | Shorthand if-else in one line | `x if condition else y` |
| **Identity** | Checks if two variables point to the SAME object in memory | `is`, `is not` |

Quick mental model:
- Arithmetic → "do math"
- Relational → "compare, get True/False"
- Logical → "combine True/False answers"
- Bitwise → "work at the binary level"
- Assignment → "store/update a value"
- Ternary → "if-else, but in one line"
- Identity → "are these the exact same object?"

*(There's also Membership operators — `in`, `not in` — used to check if a value exists inside a list/string/etc. Not covered in detail yet since you haven't reached that part.)*

---

## 3. Arithmetic Operators

These do basic math — just like a calculator.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | Float (true) Division | `5 / 2` | `2.5` |
| `//` | Floor Division | `5 // 2` | `2` |
| `%` | Modulus (remainder) | `5 % 2` | `1` |
| `**` | Exponent (power) | `5 ** 2` | `25` |

### `/` Float Division vs `//` Floor Division
Think of it like sharing candies:
- `/` gives you the exact, precise answer (with decimals) — like fair sharing down to fractions.
- `//` gives you only the **whole number part**, dropping anything after the decimal (rounds *down*, not to nearest).

```python
print(7 / 2)    # 3.5   -> exact division
print(7 // 2)   # 3     -> just the whole part, decimal dropped

print(-7 / 2)   # -3.5
print(-7 // 2)  # -4    -> ⚠️ rounds toward NEGATIVE infinity, not toward zero!
```

**Common beginner mistake:** people assume `//` just "chops off" the decimal like `int()` would. That's true for positive numbers, but for negatives, floor division goes to the *lower* number (more negative), not toward zero.

### `%` Modulus
Gives you the **remainder** left over after division. Useful for things like checking even/odd, or "does this divide evenly."

```python
print(7 % 2)    # 1  -> 7 = 2*3 + 1, remainder is 1
print(10 % 5)   # 0  -> divides evenly, no remainder

print(-7 % 2)   # 1  -> ⚠️ in Python, sign of result follows the DIVISOR (unlike C/C++ where it follows the dividend)
```

Real-world use case: `if num % 2 == 0:` → checks if a number is even.

### `**` Exponent
Raises a number to a power.

```python
print(2 ** 3)    # 8   -> 2*2*2
print(5 ** 2)    # 25  -> 5*5
print(2 ** 0.5)  # 1.414...  -> fractional power = square root
print(2 ** -1)   # 0.5 -> negative power = 1/(2**1)
```

---

## 4. Relational / Comparison Operators

These **compare two values** and always give back `True` or `False`. They're the backbone of `if` conditions and loops.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to (compares VALUE) | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `5 <= 4` | `False` |
| `is` | Same object identity (compares MEMORY LOCATION) | `a is b` | depends |
| `is not` | Different object identity | `a is not b` | depends |

### `==` vs `is` — the big beginner confusion

Analogy: imagine two identical twins wearing the same clothes.
- `==` asks: "Do they **look** the same?" → compares values/content
- `is` asks: "Are they **literally the same person**?" → compares identity (memory address)

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  -> same VALUES inside the list
print(a is b)   # False -> different objects, stored in different memory locations
print(a is c)   # True  -> c is literally pointing to the SAME object as a

print(id(a), id(b), id(c))  # id() shows the memory address
                              # a and c will show the SAME id
                              # b will show a DIFFERENT id
```

### Small int / string caching gotcha (this trips up a lot of people)

```python
x = 5
y = 5
print(x is y)   # True -> Python "caches" small integers (-5 to 256) 
                # so both x and y actually point to the SAME pre-made object

x = 500
y = 500
print(x is y)   # False (usually) -> 500 is outside the cached range,
                # so Python creates two SEPARATE objects
```

This is a classic Python interview gotcha — people expect `is` to behave like `==` for numbers because of this caching, but it's not guaranteed behavior for all values.

### ⚠️ Rule of thumb (important — memorize this)
- Use `==` for comparing values (99% of the time — numbers, strings, lists, etc.)
- Use `is` ONLY for checking identity, and its main real-world use is checking `None`:

```python
if a is None:      # ✅ correct, Pythonic way
    pass

if a == None:       # ❌ works but not recommended, avoid
    pass
```

Why? Because `None` is a singleton (only ONE `None` object ever exists in a Python program), so identity check makes sense here.

---
Logical Operators in Python

## Introduction

Logical operators are used to combine or modify conditions in Python.

They are mainly used in conditional statements such as `if`, `elif`, and `while`.

Python provides three logical operators:

1. `and`
2. `or`
3. `not`

---

## 1. AND Operator

The `and` operator returns `True` only when both conditions are `True`.

### Syntax

```python
x and y

*Note: Membership operators (`in`, `not in`) not covered yet — will add once you get to that topic.*
