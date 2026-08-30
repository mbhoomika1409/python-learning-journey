# Loops in Python

Loops are used to execute a block of code repeatedly. They are useful when we need to perform the same task multiple times.

Python mainly has two types of loops:

1. `for` loop
2. `while` loop

Python also provides loop-control statements:

* `break`
* `continue`
* `pass`

---

# 1. For Loop

A `for` loop is used to iterate over a sequence or iterable such as:

* List
* Tuple
* String
* Set
* Dictionary
* Range

## Syntax

```python
for variable in sequence:
    # code to execute
```

## Example

```python
for i in range(5):
    print(i)
```

### Output

```text
0
1
2
3
4
```

`range(5)` generates numbers from `0` to `4`.

---

# 2. range() Function

`range()` is commonly used with `for` loops to generate a sequence of numbers.

## Syntax

```python
range(start, stop, step)
```

* `start` → starting value
* `stop` → ending limit (not included)
* `step` → amount by which the value increases/decreases

## Example 1: range(stop)

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

## Example 2: range(start, stop)

```python
for i in range(2, 6):
    print(i)
```

Output:

```text
2
3
4
5
```

## Example 3: range(start, stop, step)

```python
for i in range(1, 10, 2):
    print(i)
```

Output:

```text
1
3
5
7
9
```

## Example 4: Reverse range

```python
for i in range(10, 0, -2):
    print(i)
```

Output:

```text
10
8
6
4
2
```

---

# 3. Iterating Through a String

A `for` loop can iterate through every character in a string.

```python
name = "Python"

for ch in name:
    print(ch)
```

Output:

```text
P
y
t
h
o
n
```

---

# 4. Iterating Through a List

```python
numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)
```

Output:

```text
10
20
30
40
```

---

# 5. Iterating Through a Tuple

```python
t = (10, 20, 30)

for value in t:
    print(value)
```

Output:

```text
10
20
30
```

---

# 6. Iterating Through a Set

Sets are unordered, so the order of elements may vary.

```python
s = {10, 20, 30}

for value in s:
    print(value)
```

The output may appear in a different order.

---

# 7. Iterating Through a Dictionary

## Iterate through keys

```python
student = {
    "name": "Bhoomi",
    "age": 20
}

for key in student:
    print(key)
```

Output:

```text
name
age
```

## Iterate through values

```python
for value in student.values():
    print(value)
```

Output:

```text
Bhoomi
20
```

## Iterate through keys and values

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Bhoomi
age 20
```

---

# 8. For Loop Using Index

We can access list elements using their index with `range()` and `len()`.

```python
a = ["Python", "Java", "C++"]

for i in range(len(a)):
    print(a[i])
```

Output:

```text
Python
Java
C++
```

Here:

* `len(a)` gives the number of elements.
* `range(len(a))` generates the indexes.
* `a[i]` accesses the element.

Indexes:

```text
Python → 0
Java   → 1
C++    → 2
```

---

# 9. enumerate()

`enumerate()` is a better way to get both index and value while looping.

```python
languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)
```

Output:

```text
0 Python
1 Java
2 C++
```

You can also start the index from another number:

```python
languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages, start=1):
    print(index, language)
```

Output:

```text
1 Python
2 Java
3 C++
```

---

# 10. While Loop

A `while` loop repeatedly executes a block of code as long as its condition is `True`.

## Syntax

```python
while condition:
    # code
```

## Example

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Output:

```text
0
1
2
3
4
```

### How it works

Initially:

```text
count = 0
```

Python checks:

```text
count < 5
```

If it is `True`, the loop executes.

Then:

```python
count += 1
```

increases the value.

When `count` becomes `5`:

```text
5 < 5
```

is `False`, so the loop stops.

---

# 11. Infinite While Loop

An infinite loop continues forever because its condition never becomes `False`.

```python
while True:
    print("Hello")
```

This keeps printing:

```text
Hello
Hello
Hello
...
```

Use `Ctrl + C` in the terminal to interrupt it.

Infinite loops can be useful in some programs, but they should be used carefully.

---

# 12. Nested Loops

A nested loop means one loop is placed inside another loop.

The inner loop executes completely for every iteration of the outer loop.

## Example

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

The outer loop controls `i`.

The inner loop controls `j`.

---

# 13. Nested Loop Pattern

Nested loops are commonly used to create patterns.

```python
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
```

Output:

```text
* 
* * 
* * * 
* * * *
```

`end=" "` keeps printing on the same line.

`print()` moves to the next line.

---

# 14. break Statement

`break` immediately stops the loop.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

Output:

```text
1
2
3
4
```

When `i` becomes `5`, `break` stops the loop.

---

# 15. continue Statement

`continue` skips the current iteration and moves to the next iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```text
1
2
4
5
```

When `i == 3`, Python skips `print(i)` and continues with the next iteration.

---

# 16. pass Statement

`pass` does nothing.

It is used as a placeholder when a statement is syntactically required but no action is needed yet.

```python
for i in range(5):
    pass
```

Nothing is printed.

Example:

```python
if True:
    pass
```

Later, code can be added where `pass` is written.

---

# 17. else with for Loop

Python allows an `else` block with loops.

The `else` block executes when the loop finishes normally.

```python
for i in range(5):
    print(i)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
3
4
Loop completed
```

### Important

If the loop is stopped using `break`, the `else` block does not execute.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
```

---

# 18. else with while Loop

`else` can also be used with a `while` loop.

```python
i = 1

while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed")
```

Output:

```text
1
2
3
Loop completed
```

Again, if `break` is used, the `else` block is skipped.

---

# 19. Loop Through Numbers and Check Conditions

Loops are commonly combined with `if` statements.

## Example: Even Numbers

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

Output:

```text
2
4
6
8
10
```

## Example: Odd Numbers

```python
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
```

Output:

```text
1
3
5
7
9
```

---

# 20. Sum of Numbers Using Loop

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

Output:

```text
15
```

Calculation:

```text
1 + 2 + 3 + 4 + 5 = 15
```

---

# 21. Multiplication Table

```python
n = 5

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
```

Output:

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

# 22. Find an Element Using Loop

```python
numbers = [10, 20, 30, 40]

for num in numbers:
    if num == 30:
        print("Found")
        break
```

Output:

```text
Found
```

---

# 23. Looping Through a String and Counting

```python
text = "banana"
count = 0

for ch in text:
    if ch == "a":
        count += 1

print(count)
```

Output:

```text
3
```

---

# 24. Reverse a String Using Loop

```python
text = "Python"
reverse = ""

for ch in text:
    reverse = ch + reverse

print(reverse)
```

Output:

```text
nohtyP
```

---

# 25. for Loop vs while Loop

| for loop                                        | while loop                                            |
| ----------------------------------------------- | ----------------------------------------------------- |
| Used when iterating over a sequence             | Used when a condition controls repetition             |
| Commonly used with `range()`                    | Depends on a condition                                |
| Usually used when number of iterations is known | Useful when number of iterations is unknown           |
| Example: loop through a list                    | Example: keep running until user enters correct input |

### Example

```python
for i in range(5):
    print(i)
```

Use `for` when you know what you want to iterate over.

```python
while password != "1234":
    password = input("Enter password: ")
```

Use `while` when repetition depends on a condition.

---

# 26. Important Loop Keywords

| Keyword       | Purpose                             |
| ------------- | ----------------------------------- |
| `break`       | Stops the loop completely           |
| `continue`    | Skips the current iteration         |
| `pass`        | Does nothing; acts as a placeholder |
| `range()`     | Generates a sequence of numbers     |
| `enumerate()` | Gives index and value together      |

---

# 27. Important Points to Remember

1. Python uses indentation to define the loop body.

2. `for` loops are mainly used for iterating over sequences/iterables.

3. `while` loops continue as long as the condition is `True`.

4. `range()` does not include the stop value.

```python
range(1, 5)
```

produces:

```text
1 2 3 4
```

5. `break` completely terminates the loop.

6. `continue` skips only the current iteration.

7. `pass` does nothing.

8. Loops can be nested inside other loops.

9. `for` and `while` loops can have an `else` block.

10. Be careful with `while` loops because forgetting to update the condition can create an infinite loop.

---

# Quick Revision

```text
for loop
    ↓
Iterate over sequence/iterable

while loop
    ↓
Repeat while condition is True

break
    ↓
Stop loop

continue
    ↓
Skip current iteration

pass
    ↓
Do nothing

range()
    ↓
Generate numbers

enumerate()
    ↓
Get index + value

nested loop
    ↓
Loop inside another loop

else
    ↓
Runs when loop finishes normally
```

# Simple Example Combining Everything

```python
numbers = [1, 2, 3, 4, 5]

for index, number in enumerate(numbers):
    if number == 3:
        continue

    if number == 5:
        break

    print(index, number)
```

Output:

```text
0 1
1 2
3 4
```

Here:

* `enumerate()` gives index and value.
* `continue` skips `3`.
* `break` stops the loop when the value becomes `5`.
* `for` iterates through the list.
