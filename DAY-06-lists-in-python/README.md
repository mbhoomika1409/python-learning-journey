# 🐍 Python Lists

A **list** is a built-in Python data structure used to store multiple items in a single variable.

Lists are:

* ✅ Ordered
* ✅ Mutable
* ✅ Indexed
* ✅ Dynamic / Resizable
* ✅ Allow duplicate values
* ✅ Can store different data types

---

## 1. Creating a List

### Using Square Brackets `[]`

```python
numbers = [10, 20, 30, 40]
print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

A list can contain different data types:

```python
data = [10, "Python", 3.14, True]
print(data)
```

Output:

```text
[10, 'Python', 3.14, True]
```

---

## 2. Empty List

```python
a = []
print(a)
```

Output:

```text
[]
```

You can add elements later:

```python
a.append(10)
a.append(20)

print(a)
```

Output:

```text
[10, 20]
```

---

# 3. Creating Lists Using `list()`

The `list()` constructor converts an **iterable** into a list.

### From a Tuple

```python
a = list((1, 2, 3))
print(a)
```

Output:

```text
[1, 2, 3]
```

### From a String

```python
a = list("GFG")
print(a)
```

Output:

```text
['G', 'F', 'G']
```

### Why?

A string is a sequence of individual characters.

```text
"GFG"
 ↓
 G  F  G
```

So `list("GFG")` creates one list element for each character.

> **No spaces are required between characters.**

### From Another List

```python
a = [1, 2, 3]
b = list(a)

print(b)
```

Output:

```text
[1, 2, 3]
```

---

# 4. Repeating List Elements

The `*` operator can repeat the elements of a list.

```python
a = [2] * 5
print(a)
```

Output:

```text
[2, 2, 2, 2, 2]
```

Another example:

```python
zeros = [0] * 5
print(zeros)
```

Output:

```text
[0, 0, 0, 0, 0]
```

### Important

```python
[2] * 5
```

means:

```text
[2] + [2] + [2] + [2] + [2]
```

---

# 5. List Properties

## Ordered

Lists maintain the order in which elements are inserted.

```python
a = [30, 10, 20]
print(a)
```

Output:

```text
[30, 10, 20]
```

Python does not automatically sort the list.

---

## Mutable

Lists can be changed after creation.

```python
a = [10, 20, 30]

a[1] = 50

print(a)
```

Output:

```text
[10, 50, 30]
```

---

## Allow Duplicates

```python
a = [10, 20, 10, 30, 10]

print(a)
```

Output:

```text
[10, 20, 10, 30, 10]
```

---

## Different Data Types

A single list can contain different types of values.

```python
a = [10, "Hello", 3.14, True]

print(a)
```

Output:

```text
[10, 'Hello', 3.14, True]
```

---

# 6. Indexing

Python uses **zero-based indexing**.

Example:

```python
a = [10, 20, 30, 40, 50]
```

Index positions:

```text
Value:    10    20    30    40    50
Index:     0     1     2     3     4
```

Accessing elements:

```python
print(a[0])
print(a[2])
print(a[4])
```

Output:

```text
10
30
50
```

---

# 7. Negative Indexing

Negative indexing starts from the end.

```text
Value:     10    20    30    40    50
Positive:   0     1     2     3     4
Negative:  -5    -4    -3    -2    -1
```

Example:

```python
a = [10, 20, 30, 40, 50]

print(a[-1])
print(a[-2])
```

Output:

```text
50
40
```

---

# 8. List Slicing

Slicing is used to get a portion of a list.

### Syntax

```python
list[start : stop : step]
```

Example:

```python
a = [10, 20, 30, 40, 50]

print(a[1:4])
```

Output:

```text
[20, 30, 40]
```

The `stop` index is **not included**.

### Using Step

```python
a = [10, 20, 30, 40, 50]

print(a[::2])
```

Output:

```text
[10, 30, 50]
```

### Reverse a List

```python
a = [10, 20, 30, 40, 50]

print(a[::-1])
```

Output:

```text
[50, 40, 30, 20, 10]
```

---

# 9. Adding Elements

There are three important methods:

* `append()`
* `insert()`
* `extend()`

---

## `append()`

Adds **one element** at the end.

```python
a = [1, 2]

a.append(3)

print(a)
```

Output:

```text
[1, 2, 3]
```

### Important

`append()` adds the entire object as **one element**.

```python
a = [1, 2]

a.append([3, 4])

print(a)
```

Output:

```text
[1, 2, [3, 4]]
```

---

## `insert()`

Adds an element at a specific index.

### Syntax

```python
list.insert(index, value)
```

Example:

```python
a = [1, 3]

a.insert(1, 2)

print(a)
```

Output:

```text
[1, 2, 3]
```

---

## `extend()`

Adds multiple elements to the end.

```python
a = [1, 2]

a.extend([3, 4])

print(a)
```

Output:

```text
[1, 2, 3, 4]
```

### `append()` vs `extend()`

```python
a = [1, 2]

a.append([3, 4])

print(a)
```

Output:

```text
[1, 2, [3, 4]]
```

But:

```python
a = [1, 2]

a.extend([3, 4])

print(a)
```

Output:

```text
[1, 2, 3, 4]
```

### Easy way to remember:

```text
append → adds ONE object
extend → adds elements from another iterable
```

---

# 10. Updating List Elements

Because lists are mutable, we can change elements using their index.

```python
a = [10, 20, 30]

a[1] = 200

print(a)
```

Output:

```text
[10, 200, 30]
```

We can also update multiple elements using slicing:

```python
a = [1, 2, 3, 4]

a[1:3] = [20, 30]

print(a)
```

Output:

```text
[1, 20, 30, 4]
```

---

# 11. Removing Elements

Important ways to remove elements:

* `remove()`
* `pop()`
* `del`
* `clear()`

---

## `remove()`

Removes the **first occurrence of a value**.

```python
a = [10, 20, 30, 20]

a.remove(20)

print(a)
```

Output:

```text
[10, 30, 20]
```

Only the first `20` is removed.

---

## `pop()`

Removes an element using its index and **returns the removed value**.

```python
a = [10, 20, 30]

x = a.pop()

print(x)
print(a)
```

Output:

```text
30
[10, 20]
```

By default, `pop()` removes the last element.

We can specify an index:

```python
a = [10, 20, 30]

x = a.pop(1)

print(x)
print(a)
```

Output:

```text
20
[10, 30]
```

---

## `del`

Deletes an element using its index.

```python
a = [10, 20, 30]

del a[1]

print(a)
```

Output:

```text
[10, 30]
```

It can also delete a range:

```python
a = [10, 20, 30, 40, 50]

del a[1:4]

print(a)
```

Output:

```text
[10, 50]
```

---

## `clear()`

Removes all elements.

```python
a = [10, 20, 30]

a.clear()

print(a)
```

Output:

```text
[]
```

---

# 12. Searching in a List

## `in`

Checks whether an element exists.

```python
a = [10, 20, 30]

print(20 in a)
print(50 in a)
```

Output:

```text
True
False
```

## `not in`

```python
a = [10, 20, 30]

print(50 not in a)
```

Output:

```text
True
```

---

# 13. Finding the Length

The `len()` function returns the number of elements.

```python
a = [10, 20, 30, 40]

print(len(a))
```

Output:

```text
4
```

---

# 14. Iterating Through a List

A `for` loop can be used to access every element.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
apple
banana
cherry
```

---

# 15. Iterating Using Index

We can also access elements using indexes.

```python
a = [10, 20, 30]

for i in range(len(a)):
    print(a[i])
```

Output:

```text
10
20
30
```

---

# 16. `enumerate()`

`enumerate()` gives both the index and the value.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:

```text
0 apple
1 banana
2 cherry
```

---

# 17. Nested Lists

A list can contain another list.

```python
a = [[1, 2], [3, 4]]
```

Think of it like:

```text
[
   [1, 2],
   [3, 4]
]
```

Accessing elements:

```python
print(a[0])
print(a[1][0])
```

Output:

```text
[1, 2]
3
```

### Matrix Example

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])
```

Output:

```text
6
```

---

# 18. Useful List Methods

| Method      | Purpose                            |
| ----------- | ---------------------------------- |
| `append()`  | Add one element at the end         |
| `insert()`  | Add element at a specific position |
| `extend()`  | Add multiple elements              |
| `remove()`  | Remove first matching value        |
| `pop()`     | Remove and return an element       |
| `clear()`   | Remove all elements                |
| `index()`   | Find index of a value              |
| `count()`   | Count occurrences                  |
| `sort()`    | Sort the list                      |
| `reverse()` | Reverse the list                   |
| `copy()`    | Create a copy of the list          |

---

# 19. `index()`

Returns the index of the first occurrence.

```python
a = [10, 20, 30, 20]

print(a.index(20))
```

Output:

```text
1
```

---

# 20. `count()`

Counts how many times a value appears.

```python
a = [10, 20, 20, 30, 20]

print(a.count(20))
```

Output:

```text
3
```

---

# 21. `sort()`

Sorts the list in ascending order.

```python
a = [40, 10, 30, 20]

a.sort()

print(a)
```

Output:

```text
[10, 20, 30, 40]
```

### Descending Order

```python
a.sort(reverse=True)

print(a)
```

Output:

```text
[40, 30, 20, 10]
```

---

# 22. `reverse()`

Reverses the order of elements.

```python
a = [10, 20, 30]

a.reverse()

print(a)
```

Output:

```text
[30, 20, 10]
```

---

# 23. `copy()`

Creates a copy of a list.

```python
a = [1, 2, 3]

b = a.copy()

print(b)
```

Output:

```text
[1, 2, 3]
```

---

# 24. List Assignment vs Copy

This is an important concept.

### Assignment

```python
a = [1, 2, 3]

b = a

b[0] = 100

print(a)
```

Output:

```text
[100, 2, 3]
```

Why?

Because `a` and `b` refer to the **same list object**.

### Using `copy()`

```python
a = [1, 2, 3]

b = a.copy()

b[0] = 100

print(a)
print(b)
```

Output:

```text
[1, 2, 3]
[100, 2, 3]
```

Now they are separate lists.

---

# 25. List Comprehension

List comprehension provides a short way to create lists.

### Normal Approach

```python
squares = []

for i in range(5):
    squares.append(i * i)

print(squares)
```

Output:

```text
[0, 1, 4, 9, 16]
```

### Using List Comprehension

```python
squares = [i * i for i in range(5)]

print(squares)
```

Output:

```text
[0, 1, 4, 9, 16]
```

### With Condition

```python
even = [i for i in range(10) if i % 2 == 0]

print(even)
```

Output:

```text
[0, 2, 4, 6, 8]
```

### Basic Syntax

```python
[expression for item in iterable if condition]
```

---

# 26. Built-in Functions with Lists

Python provides useful functions for lists.

```python
a = [10, 20, 30, 40]
```

### `len()`

```python
print(len(a))
```

Output:

```text
4
```

### `max()`

```python
print(max(a))
```

Output:

```text
40
```

### `min()`

```python
print(min(a))
```

Output:

```text
10
```

### `sum()`

```python
print(sum(a))
```

Output:

```text
100
```

---

# 27. Comparing Lists

Lists can be compared.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

Output:

```text
True
```

Python compares the elements and their order.

```python
a = [1, 2, 3]
b = [3, 2, 1]

print(a == b)
```

Output:

```text
False
```

Because the order is different.

---

# 28. List Concatenation

Two lists can be combined using `+`.

```python
a = [1, 2]
b = [3, 4]

c = a + b

print(c)
```

Output:

```text
[1, 2, 3, 4]
```

---

# 29. Important Difference: `append()` vs `extend()` vs `+`

```python
a = [1, 2]

a.append([3, 4])
```

Result:

```text
[1, 2, [3, 4]]
```

---

```python
a = [1, 2]

a.extend([3, 4])
```

Result:

```text
[1, 2, 3, 4]
```

---

```python
a = [1, 2]
b = [3, 4]

c = a + b
```

Result:

```text
[1, 2, 3, 4]
```

---

# 30. List Memory Concept

A Python list stores **references to objects**.

For example:

```python
a = [10, "Python", 3.14]
```

Conceptually:

```text
List
 │
 ├── reference → 10
 ├── reference → "Python"
 └── reference → 3.14
```

The list itself holds references to the objects rather than simply storing all values directly inside the list structure.

---

# 31. Mutable vs Immutable

Lists are **mutable**.

That means we can change them after creation.

```python
a = [10, 20, 30]

a[0] = 100

print(a)
```

Output:

```text
[100, 20, 30]
```

Some common mutable objects:

```text
list
dict
set
```

Some common immutable objects:

```text
int
float
str
tuple
bool
```

---

# 32. Common Errors

### IndexError

Trying to access an index that doesn't exist:

```python
a = [10, 20, 30]

print(a[5])
```

This gives:

```text
IndexError
```

because valid indexes are only:

```text
0, 1, 2
```

---

### `remove()` ValueError

```python
a = [10, 20, 30]

a.remove(50)
```

This gives:

```text
ValueError
```

because `50` is not present.

---

# 33. Quick Revision

```text
LIST
│
├── Ordered
├── Mutable
├── Indexed
├── Allows duplicates
├── Allows multiple data types
├── Dynamic / resizable
│
├── Create
│   ├── []
│   └── list()
│
├── Access
│   ├── Positive indexing
│   ├── Negative indexing
│   └── Slicing
│
├── Add
│   ├── append()
│   ├── insert()
│   └── extend()
│
├── Update
│   └── list[index] = value
│
├── Remove
│   ├── remove()
│   ├── pop()
│   ├── del
│   └── clear()
│
├── Search
│   ├── in
│   ├── not in
│   ├── index()
│   └── count()
│
├── Organize
│   ├── sort()
│   └── reverse()
│
└── Advanced
    ├── Nested lists
    ├── List comprehension
    └── Copying
```

# ⭐ Most Important Things to Remember

1. **List is ordered and mutable.**
2. **Index starts from `0`.**
3. **`-1` means the last element.**
4. **`append()` adds one object.**
5. **`extend()` adds multiple elements.**
6. **`insert()` adds at a specific position.**
7. **`remove()` removes by value.**
8. **`pop()` removes by index and returns the value.**
9. **`del` deletes using index/slice.**
10. **`clear()` removes everything.**
11. **`list("GFG")` → `['G', 'F', 'G']`.**
12. **Lists allow duplicate values.**
13. **Lists can contain different data types.**
14. **Slicing uses `[start:stop:step]`.**
15. **List comprehension is a compact way to create lists.**
