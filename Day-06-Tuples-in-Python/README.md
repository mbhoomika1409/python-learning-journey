# Python Tuples

A **tuple** is an ordered and immutable collection used to store multiple values in a single variable.

### Key Features

* **Ordered** → Elements maintain their insertion order.
* **Immutable** → Elements cannot be changed after creation.
* **Heterogeneous** → Can store different data types.
* **Indexed** → Elements can be accessed using indexes.
* **Allows duplicates** → Same value can appear multiple times.

---

## 1. Creating a Tuple

```python
# Empty tuple
t1 = ()

# Tuple with elements
t2 = (10, 20, 30)

# Tuple without parentheses
t3 = 10, 20, 30

print(t1)
print(t2)
print(t3)
```

### Output

```text
()
(10, 20, 30)
(10, 20, 30)
```

---

## 2. Single Element Tuple

A tuple containing only **one element must have a comma**.

```python
t1 = (1,)
print(type(t1))

t2 = (1)
print(type(t2))
```

### Output

```text
<class 'tuple'>
<class 'int'>
```

👉 `(1,)` → Tuple
👉 `(1)` → Integer

---

## 3. Tuple with Different Data Types

Tuples can contain different types of data.

```python
tup = (10, "Python", 3.14, True)

print(tup)
```

### Output

```text
(10, 'Python', 3.14, True)
```

---

## 4. Accessing Tuple Elements

Tuple indexing starts from **0**.

```python
t2 = ('Geeks', 'For', 'Geeks', 1, 2)

print(t2[0])
print(t2[3])
print(t2[4])
```

### Output

```text
Geeks
1
2
```

### Negative Indexing

Negative indexing starts from `-1` at the last element.

```python
t2 = ('Geeks', 'For', 'Geeks', 1, 2)

print(t2[-1])
print(t2[-2])
print(t2[-3])
```

### Output

```text
2
1
Geeks
```

---

## 5. Tuple Slicing

Slicing is used to get a part of a tuple.

### Syntax

```python
tuple[start:stop:step]
```

```python
tup = (10, 20, 30, 40, 50)

print(tup[1:4])
print(tup[:3])
print(tup[2:])
print(tup[::-1])
```

### Output

```text
(20, 30, 40)
(10, 20, 30)
(30, 40, 50)
(50, 40, 30, 20, 10)
```

---

## 6. Tuple is Immutable

We cannot change an existing tuple element.

```python
tup = (10, 20, 30)

tup[0] = 100
```

### Output

```text
TypeError
```

❌ This is not allowed because tuples are immutable.

---

## 7. Concatenation

The `+` operator joins two tuples.

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

t3 = t1 + t2

print(t3)
```

### Output

```text
(1, 2, 3, 4, 5, 6)
```

---

## 8. Repetition

The `*` operator repeats a tuple.

```python
tup = (1, 2)

print(tup * 3)
```

### Output

```text
(1, 2, 1, 2, 1, 2)
```

---

## 9. Checking an Element

Use `in` and `not in` to check whether an element exists.

```python
tup = (10, 20, 30, 40)

print(20 in tup)
print(50 in tup)
print(50 not in tup)
```

### Output

```text
True
False
True
```

---

## 10. Tuple Length

Use `len()` to find the number of elements.

```python
tup = (10, 20, 30, 40)

print(len(tup))
```

### Output

```text
4
```

---

## 11. Tuple Unpacking

Tuple unpacking assigns tuple elements to separate variables.

```python
tup = ("Python", "Java", "C++")

a, b, c = tup

print(a)
print(b)
print(c)
```

### Output

```text
Python
Java
C++
```

---

## 12. Tuple Unpacking with `*`

`*` collects multiple remaining elements into a **list**.

```python
tup = (1, 2, 3, 4, 5)

a, *b, c = tup

print(a)
print(b)
print(c)
```

### Output

```text
1
[2, 3, 4]
5
```

Here:

* `a` → first element
* `*b` → middle elements
* `c` → last element

---

## 13. Counting Elements

`count()` tells how many times an element occurs.

```python
tup = (1, 2, 2, 3, 2, 4)

print(tup.count(2))
```

### Output

```text
3
```

---

## 14. Finding Index

`index()` returns the position of the first occurrence of an element.

```python
tup = (10, 20, 30, 40)

print(tup.index(30))
```

### Output

```text
2
```

---

## 15. Converting List to Tuple

Use `tuple()` to convert a list into a tuple.

```python
li = [1, 2, 3, 4]

tup = tuple(li)

print(tup)
print(type(tup))
```

### Output

```text
(1, 2, 3, 4)
<class 'tuple'>
```

---

## 16. Converting Tuple to List

Use `list()` to convert a tuple into a list.

```python
tup = (1, 2, 3, 4)

li = list(tup)

print(li)
print(type(li))
```

### Output

```text
[1, 2, 3, 4]
<class 'list'>
```

This is useful when you need to modify tuple data.

---

## 17. Deleting a Tuple

Individual elements cannot be deleted because tuples are immutable.

However, the complete tuple can be deleted using `del`.

```python
tup = (1, 2, 3)

del tup
```

After deletion, `tup` no longer exists.

---

## 18. Nested Tuples

A tuple can contain another tuple.

```python
tup = (1, 2, (3, 4), 5)

print(tup[2])
print(tup[2][0])
```

### Output

```text
(3, 4)
3
```

---

## 19. Tuple Methods

Tuples mainly have two built-in methods:

### `count()`

Counts how many times a value appears.

```python
tup = (1, 2, 2, 3)

print(tup.count(2))
```

### `index()`

Returns the index of the first occurrence.

```python
tup = (10, 20, 30)

print(tup.index(20))
```

---

## 20. Useful Built-in Functions

Python provides several functions that work with tuples.

```python
tup = (10, 20, 30, 40)

print(len(tup))
print(max(tup))
print(min(tup))
print(sum(tup))
```

### Output

```text
4
40
10
100
```

---

## 21. Tuple vs List

| Feature              | Tuple | List  |
| -------------------- | ----- | ----- |
| Syntax               | `()`  | `[]`  |
| Ordered              | Yes   | Yes   |
| Mutable              | ❌ No  | ✅ Yes |
| Allows duplicates    | Yes   | Yes   |
| Different data types | Yes   | Yes   |
| Indexing             | Yes   | Yes   |
| Slicing              | Yes   | Yes   |
| Methods              | Fewer | More  |

### Example

```python
# List
my_list = [1, 2, 3]
my_list[0] = 100

# Tuple
my_tuple = (1, 2, 3)
# my_tuple[0] = 100  # Error
```

---

## 22. Your Practice Code

```python
# Single element tuple
t1 = (1,)
print(type(t1))

# Accessing tuple elements
t2 = ('Geeks', 'For', 'Geeks', 1, 2)

print(t2[3])
print(t2[-3])
```

### Output

```text
<class 'tuple'>
1
Geeks
```

---

## 23. Important Points to Remember ⭐

```text
Tuple = Ordered + Immutable + Indexed + Allows Duplicates
```

### Remember:

```python
(1,)       # Tuple
(1)        # Integer

tup[0]     # Access element
tup[-1]    # Last element
tup[1:4]   # Slicing
tup[::-1]  # Reverse tuple

len(tup)   # Number of elements
tup.count()# Count occurrence
tup.index()# Find index

tuple(list) # List → Tuple
list(tuple) # Tuple → List
```

### Real-world use

Tuples are useful when data **should not change**, for example:

```python
student = ("Bhoomika", 21, "AIML")
coordinates = (15.5, 75.6)
rgb = (255, 0, 0)
```

Because tuples are immutable, they are useful for storing fixed data.
