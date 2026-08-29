# Python Dictionary

A **dictionary** is a built-in Python data type that stores data in **key-value pairs**.

```python
student = {
    "name": "Bhoomi",
    "age": 20,
    "branch": "AIML"
}
```

Here:

```text
"name"   → Key
"Bhoomi" → Value

"age"    → Key
20       → Value
```

### ⭐ Main Features

* Stores data as **key : value** pairs.
* Keys must be **unique**.
* Keys must be **hashable** (commonly strings, numbers, tuples containing hashable elements).
* Values can be of different data types.
* Dictionaries are **mutable**.
* Values are accessed using **keys**, not indexes.
* Dictionaries preserve **insertion order** in modern Python.

---

# 1. Creating a Dictionary

```python
d = {
    "name": "Sam",
    "age": 20
}

print(d)
```

Output:

```text
{'name': 'Sam', 'age': 20}
```

You can also use `dict()`:

```python
d = dict(name="Sam", age=20)

print(d)
```

Output:

```text
{'name': 'Sam', 'age': 20}
```

---

# 2. Key and Value

Consider:

```python
d = {
    "name": "Sam",
    "age": 20
}
```

```text
"name" → Key
"Sam"  → Value

"age"  → Key
20     → Value
```

The general structure is:

```python
{
    key: value,
    key: value
}
```

---

# 3. Keys Must Be Unique

A dictionary cannot have duplicate keys.

```python
d = {
    "name": "Sam",
    "name": "Alex"
}

print(d)
```

Output:

```text
{'name': 'Alex'}
```

The second `"name"` replaces the first value.

### ⭐ Remember

```text
Duplicate keys → Not allowed
Duplicate values → Allowed
```

Example:

```python
d = {
    "student1": "Sam",
    "student2": "Sam"
}
```

This is completely valid because the **keys are different**.

---

# 4. Accessing Dictionary Values

Use the key inside square brackets.

```python
d = {
    "name": "Sam",
    "age": 20
}

print(d["name"])
print(d["age"])
```

Output:

```text
Sam
20
```

### Important

Dictionary:

```python
d["name"]
```

List:

```python
li[0]
```

So:

```text
List       → Access using index
Dictionary → Access using key
```

---

# 5. Using `get()`

We can also use `get()` to access a value.

```python
d = {
    "name": "Sam",
    "age": 20
}

print(d.get("name"))
```

Output:

```text
Sam
```

### `[]` vs `get()`

If the key doesn't exist:

```python
d["city"]
```

❌ Raises `KeyError`.

But:

```python
d.get("city")
```

returns:

```text
None
```

We can also provide a default value:

```python
print(d.get("city", "Not Found"))
```

Output:

```text
Not Found
```

### ⭐ Remember

```text
d["key"]       → Error if key doesn't exist
d.get("key")   → None if key doesn't exist
```

---

# 6. Adding a New Item

Simply assign a value to a new key.

```python
d = {
    "name": "Sam"
}

d["age"] = 20

print(d)
```

Output:

```text
{'name': 'Sam', 'age': 20}
```

---

# 7. Updating an Existing Item

If the key already exists, its value is updated.

```python
d = {
    "name": "Sam",
    "age": 20
}

d["age"] = 21

print(d)
```

Output:

```text
{'name': 'Sam', 'age': 21}
```

### ⭐ Same syntax does two things:

```python
d["key"] = value
```

```text
New key      → Adds
Existing key → Updates
```

---

# 8. Dictionary is Mutable

Dictionaries can be changed after creation.

```python
d = {
    "name": "Sam",
    "age": 20
}

d["age"] = 21
d["city"] = "Bangalore"

print(d)
```

The dictionary has been modified.

---

# 9. Removing an Item Using `del`

`del` removes an item using its key.

```python
d = {
    "name": "Sam",
    "age": 20
}

del d["age"]

print(d)
```

Output:

```text
{'name': 'Sam'}
```

---

# 10. `pop()`

`pop()` removes the specified key and **returns its value**.

```python
d = {
    "name": "Sam",
    "age": 20
}

x = d.pop("age")

print(x)
print(d)
```

Output:

```text
20
{'name': 'Sam'}
```

### ⭐ Remember

```text
del       → Removes item
pop(key)  → Removes item + returns its value
```

---

# 11. `popitem()`

`popitem()` removes and returns the **last inserted key-value pair**.

```python
d = {
    "name": "Sam",
    "age": 20,
    "city": "Bangalore"
}

x = d.popitem()

print(x)
print(d)
```

Output:

```text
('city', 'Bangalore')
{'name': 'Sam', 'age': 20}
```

The returned pair is a **tuple**:

```python
('city', 'Bangalore')
```

---

# 12. `clear()`

`clear()` removes all items.

```python
d = {
    "name": "Sam",
    "age": 20
}

d.clear()

print(d)
```

Output:

```text
{}
```

---

# 13. Checking if a Key Exists

Use `in`.

```python
d = {
    "name": "Sam",
    "age": 20
}

print("name" in d)
print("city" in d)
```

Output:

```text
True
False
```

### Important

`in` checks **keys** by default.

```python
"name" in d
```

✅ Checks whether `"name"` is a key.

---

# 14. Getting All Keys

Use `keys()`.

```python
d = {
    "name": "Sam",
    "age": 20
}

print(d.keys())
```

Output:

```text
dict_keys(['name', 'age'])
```

You can loop through them:

```python
for key in d.keys():
    print(key)
```

Output:

```text
name
age
```

---

# 15. Getting All Values

Use `values()`.

```python
d = {
    "name": "Sam",
    "age": 20
}

print(d.values())
```

Output:

```text
dict_values(['Sam', 20])
```

Loop:

```python
for value in d.values():
    print(value)
```

Output:

```text
Sam
20
```

---

# 16. Getting Keys and Values Together

Use `items()`.

```python
d = {
    "name": "Sam",
    "age": 20
}

print(d.items())
```

Output:

```text
dict_items([('name', 'Sam'), ('age', 20)])
```

Each key-value pair is represented as a **tuple**.

---

# 17. Iterating Through a Dictionary

### Only keys

```python
d = {
    "name": "Sam",
    "age": 20
}

for key in d:
    print(key)
```

Output:

```text
name
age
```

### Only values

```python
for value in d.values():
    print(value)
```

### Both key and value

```python
for key, value in d.items():
    print(key, value)
```

Output:

```text
name Sam
age 20
```

### ⭐ Most useful pattern

```python
for key, value in d.items():
    print(key, value)
```

---

# 18. Dictionary with Different Data Types

Values can contain different data types.

```python
d = {
    "name": "Sam",
    "age": 20,
    "marks": 85.5,
    "passed": True
}

print(d)
```

Values can be:

```text
String
Integer
Float
Boolean
List
Tuple
Dictionary
etc.
```

---

# 19. Nested Dictionary

A dictionary can contain another dictionary as a value.

```python
students = {
    "student1": {
        "name": "Sam",
        "age": 20
    },
    "student2": {
        "name": "Alex",
        "age": 21
    }
}
```

Access nested values:

```python
print(students["student1"]["name"])
```

Output:

```text
Sam
```

Think:

```text
students
   ↓
student1
   ↓
name
   ↓
Sam
```

---

# 20. Dictionary with List as Value

Values can also be lists.

```python
student = {
    "name": "Sam",
    "marks": [80, 85, 90]
}

print(student["marks"])
```

Output:

```text
[80, 85, 90]
```

Access a particular mark:

```python
print(student["marks"][0])
```

Output:

```text
80
```

---

# 21. `update()`

`update()` adds new key-value pairs or updates existing ones.

```python
d = {
    "name": "Sam",
    "age": 20
}

d.update({
    "age": 21,
    "city": "Bangalore"
})

print(d)
```

Output:

```text
{'name': 'Sam', 'age': 21, 'city': 'Bangalore'}
```

Here:

```text
age  → Updated
city → Added
```

---

# 22. `setdefault()`

`setdefault()` returns the value of a key.

If the key doesn't exist, it adds the key with the given default value.

```python
d = {
    "name": "Sam"
}

x = d.setdefault("age", 20)

print(x)
print(d)
```

Output:

```text
20
{'name': 'Sam', 'age': 20}
```

If the key already exists, it doesn't replace its value.

---

# 23. `fromkeys()`

`fromkeys()` creates a dictionary using a sequence of keys.

```python
keys = ["name", "age", "city"]

d = dict.fromkeys(keys)

print(d)
```

Output:

```text
{'name': None, 'age': None, 'city': None}
```

You can provide a default value:

```python
d = dict.fromkeys(keys, "Unknown")

print(d)
```

Output:

```text
{'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}
```

---

# 24. Dictionary Length

Use `len()` to find the number of key-value pairs.

```python
d = {
    "name": "Sam",
    "age": 20,
    "city": "Bangalore"
}

print(len(d))
```

Output:

```text
3
```

---

# 25. Dictionary Comprehension

A short way to create dictionaries.

```python
squares = {x: x * x for x in range(1, 5)}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16}
```

Structure:

```python
{key: value for item in iterable}
```

---

# 26. Dictionary vs List vs Set vs Tuple

| Feature    | List  | Tuple | Set                   | Dictionary        |
| ---------- | ----- | ----- | --------------------- | ----------------- |
| Syntax     | `[]`  | `()`  | `{}`                  | `{key: value}`    |
| Ordered    | ✅     | ✅     | ❌ No guaranteed order | ✅ Insertion order |
| Mutable    | ✅     | ❌     | ✅                     | ✅                 |
| Duplicates | ✅     | ✅     | ❌                     | Keys ❌, Values ✅  |
| Indexing   | ✅     | ✅     | ❌                     | ❌                 |
| Access     | Index | Index | Membership            | Key               |

---

# 27. ⭐ Important Dictionary Methods

| Method         | Purpose                     |
| -------------- | --------------------------- |
| `get()`        | Get value safely            |
| `keys()`       | Get all keys                |
| `values()`     | Get all values              |
| `items()`      | Get key-value pairs         |
| `update()`     | Add/update multiple items   |
| `pop()`        | Remove specified key        |
| `popitem()`    | Remove last inserted pair   |
| `clear()`      | Remove everything           |
| `setdefault()` | Get/add a default value     |
| `fromkeys()`   | Create dictionary from keys |

---

# 28. Simple Complete Example

```python
student = {
    "name": "Bhoomi",
    "age": 20,
    "branch": "AIML"
}

# Access
print(student["name"])

# Add
student["city"] = "Davangere"

# Update
student["age"] = 21

# Check key
print("branch" in student)

# Keys
print(student.keys())

# Values
print(student.values())

# Key-value pairs
for key, value in student.items():
    print(key, value)
```

---

# ⭐ Quick Revision

```text
Dictionary
     ↓
Key : Value
     ↓
Keys are unique
     ↓
Access using keys
     ↓
Mutable
     ↓
Fast lookup using hashing
```

### Basic syntax

```python
student = {
    "name": "Bhoomi",
    "age": 20
}
```

### Access

```python
student["name"]
student.get("name")
```

### Add / Update

```python
student["city"] = "Bangalore"
student["age"] = 21
```

### Delete

```python
del student["age"]
student.pop("city")
student.popitem()
student.clear()
```

### Iterate

```python
for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)
```

### ⭐ One-Line Definition

> **A dictionary is a mutable Python data structure that stores data as unique key-value pairs and allows values to be efficiently accessed using their keys.**
