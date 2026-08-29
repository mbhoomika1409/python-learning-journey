# Python Set Data Type

A **set** is a built-in Python data type used to store a collection of **unique elements**.

### Main Features

* **Unique** → Duplicate elements are automatically removed.
* **Unordered** → Elements don't have a guaranteed order.
* **No indexing** → We cannot access elements using `s[0]`.
* **Mutable** → We can add and remove elements.
* **Heterogeneous** → Can contain different data types.
* **Fast lookup** → Uses a hash-table-based implementation internally.

---

# 1. Creating a Set

A set is created using `{}` with elements separated by commas.

```python
s = {10, 50, 20}

print(s)
print(type(s))
```

Output:

```text
{10, 50, 20}
<class 'set'>
```

⚠️ The order may be different when printed.

---

# 2. Empty Set

Be careful:

```python
s = {}
print(type(s))
```

Output:

```text
<class 'dict'>
```

`{}` creates an **empty dictionary**.

To create an empty set:

```python
s = set()

print(s)
print(type(s))
```

Output:

```text
set()
<class 'set'>
```

---

# 3. Duplicate Elements

Sets automatically remove duplicate values.

```python
s = {"a", "a", "b", "c", "b"}

print(s)
```

Output may be:

```text
{'a', 'b', 'c'}
```

So:

```text
"a" → repeated → removed
"b" → repeated → removed
```

Only unique elements remain.

---

# 4. Set is Unordered

Sets do not maintain a guaranteed order.

```python
s = {"a", "b", "c"}

print(s)
```

You might see:

```text
{'a', 'b', 'c'}
```

or another order.

### ⭐ Remember

```text
List  → Ordered
Tuple → Ordered
Set   → Unordered
```

Therefore, don't depend on the order in which a set is printed or iterated.

---

# 5. No Indexing

Lists allow indexing:

```python
li = [10, 20, 30]

print(li[0])
```

But sets don't:

```python
s = {10, 20, 30}

print(s[0])
```

This produces an error because sets don't have fixed positions.

---

# 6. Accessing Set Elements

Since sets don't support indexing, we normally access their elements using a `for` loop.

```python
s = {"Geeks", "For", "Python"}

for i in s:
    print(i)
```

The order of output is not guaranteed.

---

# 7. Heterogeneous Elements

Sets can contain different data types.

```python
s = {"Python", 10, 52.7, True}

print(s)
```

A set can contain values such as:

```text
String
Integer
Float
Boolean
```

However, set elements must be **hashable**.

---

# 8. Sets Are Mutable

A set itself can be changed.

We can:

* Add elements
* Remove elements
* Clear elements

Example:

```python
s = {1, 2, 3}

s.add(4)

print(s)
```

Output:

```text
{1, 2, 3, 4}
```

But we cannot modify an element using an index:

```python
s[0] = 100
```

❌ Error.

---

# 9. `set()` Function

The `set()` function creates a set or converts another iterable into a set.

### Syntax

```python
set(iterable)
```

Example:

```python
s = set(["a", "b", "c"])

print(s)
```

Output may be:

```text
{'a', 'b', 'c'}
```

---

# 10. List → Set

```python
a = [1, 2, 2, 3]

s = set(a)

print(s)
```

Output:

```text
{1, 2, 3}
```

The duplicate `2` is removed.

---

# 11. Tuple → Set

```python
t = (1, 1, 2, 3)

s = set(t)

print(s)
```

Output:

```text
{1, 2, 3}
```

---

# 12. String → Set

```python
s = set("hello")

print(s)
```

Output contains unique characters, for example:

```text
{'h', 'e', 'l', 'o'}
```

The repeated `l` is removed.

---

# 13. Range → Set

```python
s = set(range(3, 8))

print(s)
```

Output:

```text
{3, 4, 5, 6, 7}
```

---

# 14. Dictionary → Set

When a dictionary is passed to `set()`, only its **keys** are included.

```python
d = {"x": 1, "y": 2, "z": 3}

s = set(d)

print(s)
```

Output contains:

```text
{'x', 'y', 'z'}
```

The dictionary values are not included.

---

# 15. `add()`

`add()` adds one element to a set.

```python
s = {"a", "b", "c"}

s.add("d")

print(s)
```

Output may be:

```text
{'a', 'b', 'c', 'd'}
```

If the element already exists, nothing is added again.

```python
s.add("a")
```

The set still contains only one `"a"`.

---

# 16. `remove()`

`remove()` removes a specific element.

```python
s = {1, 2, 3, 4}

s.remove(3)

print(s)
```

Output:

```text
{1, 2, 4}
```

⚠️ If the element doesn't exist, `remove()` raises a `KeyError`.

---

# 17. `discard()`

`discard()` also removes an element.

```python
s = {1, 2, 3}

s.discard(2)

print(s)
```

Output:

```text
{1, 3}
```

The difference:

```text
remove()  → Error if element doesn't exist
discard() → No error if element doesn't exist
```

---

# 18. `pop()`

`pop()` removes and returns an arbitrary element from the set.

```python
s = {10, 20, 30}

x = s.pop()

print(x)
print(s)
```

⚠️ Don't expect a particular element to be removed because sets are unordered.

---

# 19. `clear()`

`clear()` removes all elements.

```python
s = {1, 2, 3}

s.clear()

print(s)
```

Output:

```text
set()
```

---

# 20. Union

**Union** means combining all unique elements from both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
```

Output:

```text
{1, 2, 3, 4, 5}
```

### Using `|`

```python
print(a | b)
```

Same result.

### Remember:

```text
Union → EVERYTHING from both sets
```

---

# 21. Intersection

**Intersection** means elements that are common to both sets.

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))
```

Output:

```text
{2, 3}
```

### Using `&`

```python
print(a & b)
```

Same result.

### Remember:

```text
Intersection → COMMON elements
```

---

# 22. Difference

Difference returns elements that are in the **first set but not the second**.

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.difference(b))
```

Output:

```text
{1}
```

### Using `-`

```python
print(a - b)
```

Same result.

### Important

```text
a - b → Elements in a but NOT in b
b - a → Elements in b but NOT in a
```

---

# 23. Symmetric Difference

Returns elements that are in **either set, but not in both**.

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.symmetric_difference(b))
```

Output:

```text
{1, 4}
```

### Using `^`

```python
print(a ^ b)
```

Same result.

Think:

```text
a → 1 2 3
b →   2 3 4

Common → 2, 3 ❌
Only one set → 1, 4 ✅
```

---

# 24. Membership Operators

Use `in` to check whether an element exists.

```python
s = {10, 20, 30}

print(20 in s)
print(50 in s)
```

Output:

```text
True
False
```

Use `not in`:

```python
print(50 not in s)
```

Output:

```text
True
```

---

# 25. Subset

A set is a **subset** if all its elements are present in another set.

```python
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
```

Output:

```text
True
```

Because every element of `a` exists in `b`.

### Using `<=`

```python
print(a <= b)
```

---

# 26. Superset

A set is a **superset** if it contains all elements of another set.

```python
a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b))
```

Output:

```text
True
```

### Using `>=`

```python
print(a >= b)
```

---

# 27. Frozenset

A `frozenset` is an **immutable version of a set**.

```python
fs = frozenset([1, 2, 3])

print(fs)
```

You cannot do:

```python
fs.add(4)
```

❌ Error.

Normal set:

```text
set → Mutable
```

Frozen set:

```text
frozenset → Immutable
```

Frozensets can also be used where a hashable object is required, such as a dictionary key.

---

# 28. Internal Working of Set

Python sets use a **hash-table-based implementation** internally.

The basic idea is:

```text
Element
   ↓
Hash
   ↓
Hash table location
   ↓
Store / find element
```

For example:

```python
s = {10, 20, 30}
```

Python calculates hash information for the elements and uses the hash table to efficiently find them.

This is why:

```python
20 in s
```

is generally very fast.

### Collision

Sometimes two different elements can initially map to the same table location.

This is called a **collision**.

Python has mechanisms to resolve these collisions and find suitable slots.

You don't need the low-level implementation details for basic Python.

### ⭐ Remember

```text
Set
 ↓
Hash table
 ↓
Fast lookup
```

---

# 29. Set Operators

| Operator     | Meaning                        |
| ------------ | ------------------------------ |
| `x in s`     | Check if x exists              |
| `x not in s` | Check if x doesn't exist       |
| `a == b`     | Sets contain the same elements |
| `a != b`     | Sets are different             |
| `a \| b`     | Union                          |
| `a & b`      | Intersection                   |
| `a - b`      | Difference                     |
| `a ^ b`      | Symmetric difference           |
| `a <= b`     | Subset                         |
| `a < b`      | Proper subset                  |
| `a >= b`     | Superset                       |
| `a > b`      | Proper superset                |

---

# 30. Important Set Methods

| Method                   | Purpose                               |
| ------------------------ | ------------------------------------- |
| `add()`                  | Add an element                        |
| `remove()`               | Remove an element; error if absent    |
| `discard()`              | Remove an element; no error if absent |
| `pop()`                  | Remove an arbitrary element           |
| `clear()`                | Remove everything                     |
| `union()`                | Combine sets                          |
| `intersection()`         | Common elements                       |
| `difference()`           | Elements only in first set            |
| `symmetric_difference()` | Elements in exactly one set           |
| `issubset()`             | Check subset                          |
| `issuperset()`           | Check superset                        |

---

# 31. Quick Example

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)
```

Output:

```text
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference: {1, 2}
Symmetric Difference: {1, 2, 5, 6}
```

---

# 32. ⭐ Quick Revision

```text
Set
 ↓
Unique elements
 ↓
Unordered
 ↓
No indexing
 ↓
Mutable
 ↓
Fast lookup using hashing
```

### Creating:

```python
s = {1, 2, 3}
```

### Empty set:

```python
s = set()
```

### Convert:

```python
set([1, 2, 2, 3])
# {1, 2, 3}
```

### Main operations:

```python
a | b    # Union
a & b    # Intersection
a - b    # Difference
a ^ b    # Symmetric difference
```

### Main methods:

```python
s.add(x)
s.remove(x)
s.discard(x)
s.pop()
s.clear()
```

### ⭐ One-Line Definition

> **A set is an unordered, mutable collection of unique elements that provides efficient membership checking using a hash-table-based implementation.**
