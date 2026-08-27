# Python Strings — Notes

## 📌 Today's Topics — Python Strings

1. Sequence Data Types (intro)
2. Creating a String (single/double/triple quotes)
3. Accessing Characters (indexing — positive & negative)
4. String Slicing (`start:end:step`, negative indexing, reversing)
5. Looping Through Strings
6. String Immutability
7. Deleting a String (`del`)
8. Updating a String (via slicing/methods)
9. Common String Methods (`len()`, `upper()`, `lower()`, `strip()`, `replace()`)
10. Concatenation & Repetition (`+`, `*`)
11. Formatting Strings (f-strings, `.format()`)
12. String Membership Testing (`in`)

Topics covered: Sequence Data Types intro, String basics, Indexing, Slicing, Immutability, Methods, Formatting, Membership Testing.

---

## 1. Sequence Data Types

A **sequence** is an ordered collection of items (similar or different types). Elements can be accessed using indexing.

**String** is one type of sequence — used to store text data, represented by the `str` class.

```python
s = 'Welcome to the Geeks World'
print(s)
print(type(s))        # <class 'str'>

# access string with index
print(s[1])            # e
print(s[-1])           # d
```

---

## 2. Creating a String

Strings can use single `'...'`, double `"..."`, or triple quotes `'''...'''` / `"""..."""`. Single/double behave the same.

```python
a = 'GFG'
b = "GeeksForGeeks"
print(a)   # GFG
print(b)   # GeeksForGeeks
```

**Multi-line strings** — use triple quotes; newlines are preserved.

```python
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)
```

---

## 3. Indexing

Strings are indexed sequences.
- **Positive index** → starts at `0` from the left
- **Negative index** → starts at `-1` from the right

```python
s = "ABCDEF"
print(s[0])    # A
print(s[4])    # E
print(s[-3])   # D
print(s[-5])   # B
```

⚠️ Out-of-range index → `IndexError`
⚠️ Non-integer index (float, etc.) → `TypeError`

---

## 4. Slicing

Syntax: `s[start : end : step]`

| Part | Meaning | Default |
|------|---------|---------|
| start | inclusive starting index | 0 |
| end | exclusive stopping index | end of string |
| step | interval between indices (negative = right→left) | 1 |

Return type is always a new `str`.

```python
s = "ABCDEF"
print(s[1:4])     # BCD
print(s[:3])       # ABC
print(s[3:])       # DEF
print(s[::-1])     # FEDCBA (reverse)
```

**Negative indexing in slicing:**

```python
s = "abcdefghijklmno"
print(s[-4:])        # lmno
print(s[:-3])         # abcdefghijkl
print(s[-5:-2])       # klm
print(s[-8:-1:2])     # hjln
```

**Get the full string:**

```python
s = "Hello, World!"
print(s[:])    # Hello, World!
print(s[::])   # Hello, World!
```

**Step examples:**

```python
s = "abcdefghi"
print(s[::2])       # acegi   (every 2nd char)
print(s[1:8:3])      # beh     (every 3rd char, index 1 to 8)
```

---

## 5. Looping Through Strings

```python
s = "ABCDEF"
for char in s:
    print(char)
```
Loop goes in order, printing each character on every iteration.

---

## 6. String Immutability

Strings **cannot be changed** after creation. Any "modification" creates a **new** string.

```python
s = "aBCDEF"
s = "A" + s[1:]
print(s)   # ABCDEF
```

**Deleting** a string variable (not individual chars) uses `del`:

```python
s = "ABC"
del s
# accessing s now → NameError
```

**"Updating"** a string = building a new one via slicing/methods:

```python
s = "ABCD EF"
s1 = "H" + s[1:]                 # HBCD EF
s2 = s.replace("ABC", "abc")     # abcD EF
```

---

## 7. Common String Methods

| Method | Purpose |
|--------|---------|
| `len(s)` | total number of characters |
| `s.upper()` | convert to uppercase |
| `s.lower()` | convert to lowercase |
| `s.strip()` | remove leading/trailing whitespace |
| `s.replace(old, new)` | replace all occurrences of a substring |

```python
s = "GeeksforGeeks"
print(len(s))          # 13

s = "Hello World"
print(s.upper())        # HELLO WORLD
print(s.lower())        # hello world

s = "   ABC   "
print(s.strip())        # ABC

s = "Python is fun"
print(s.replace("fun", "awesome"))   # Python is awesome
```

---

## 8. Concatenation and Repetition

```python
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)    # Hello World

s = "Hello "
print(s * 3)             # Hello Hello Hello
```

---

## 9. Formatting Strings

**f-strings:**

```python
name = "Jake"
age = 22
print(f"Name: {name}, Age: {age}")
```

**`.format()` method:**

```python
s = "My name is {} and I am {} years old.".format("Emily", 22)
print(s)
```

---

## 10. Membership Testing

`in` keyword checks whether a substring exists inside a string → returns `True`/`False`.

```python
s = "GeeksforGeeks"
print("Geeks" in s)   # True
print("GfG" in s)      # False
```

---

## Quick Recap

- Strings = immutable sequences of characters, no separate "char" type in Python.
- Indexing: positive (0 → left) and negative (-1 → right).
- Slicing: `[start:end:step]`, always returns a new string.
- Any "update" = new string via slicing/methods, original never changes.
- Key methods: `len()`, `upper()`, `lower()`, `strip()`, `replace()`.
- Formatting: f-strings (`f"{var}"`) or `.format()`.
- `in` keyword for substring membership check.
