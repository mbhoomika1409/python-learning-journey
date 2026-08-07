# 🐍 Day 01 - Python Fundamentals

## 📅 Date
**07 August 2026**

---

# 1. Introduction to Python

Python is a high-level, interpreted, object-oriented, and general-purpose programming language developed by **Guido van Rossum** and first released in **1991**.

Python is known for its simple syntax, readability, and vast ecosystem of libraries, making it one of the most popular programming languages today.

---

# 2. Python Basics

### What is Python?

Python is an interpreted programming language that allows developers to write clean and efficient code.

### Characteristics

- Easy to learn
- Easy to read
- High-level language
- Interpreted language
- Cross-platform
- Open-source
- Object-oriented

---

# 3. Comments in Python

Comments are used to explain code and improve readability.

### Single-line Comment

```python
# This is a single-line comment
print("Hello, World!")
```

### Multi-line Comment

```python
"""
This is a
multi-line comment.
"""
```

---

# 4. Applications of Python

Python is widely used in various domains.

- Web Development
- Machine Learning
- Artificial Intelligence
- Data Science
- Automation
- Cybersecurity
- Desktop Applications
- Game Development
- Cloud Computing
- Internet of Things (IoT)

---

# 5. Advantages of Python

- Simple and readable syntax
- Easy to learn
- Large standard library
- Cross-platform support
- Huge developer community
- Open-source
- Supports multiple programming paradigms
- Rapid application development

---

# 6. Disadvantages of Python

- Slower execution compared to compiled languages
- High memory consumption
- Less suitable for mobile app development
- Not ideal for low-level system programming

---

# 7. Python Web Development with Django

## What is Django?

Django is a high-level Python web framework that enables rapid development of secure, scalable, and maintainable web applications.

### Features

- Built-in Admin Panel
- Authentication System
- URL Routing
- ORM (Object Relational Mapping)
- Security Features
- Scalable Architecture

---

# 8. Django Architecture (MVT Pattern)

Django follows the **MVT (Model-View-Template)** architecture.

### Model

- Handles database operations.
- Defines the structure of data.

### View

- Contains the application logic.
- Processes user requests.

### Template

- Responsible for displaying data to users.
- Creates the user interface using HTML.

---

# 9. MVT Workflow

The request flow in Django is:

```
User Request
      │
      ▼
URL Configuration (urls.py)
      │
      ▼
View (views.py)
      │
      ▼
Model (models.py)
      │
      ▼
Database
      │
      ▼
Template (HTML)
      │
      ▼
HTTP Response
```

---

# 10. Django ORM (Object Relational Mapping)

ORM allows developers to interact with the database using Python code instead of SQL queries.

### Common ORM Methods

```python
Model.objects.create()

Model.objects.all()

Model.objects.get()

Model.objects.filter()

Model.objects.update()

Model.objects.delete()
```

---

# 11. CRUD Operations

CRUD stands for:

### Create (Insert)

```python
Student.objects.create(name="John")
```

### Read (Retrieve)

```python
Student.objects.all()
```

### Update

```python
student = Student.objects.get(id=1)
student.name = "David"
student.save()
```

### Delete

```python
student = Student.objects.get(id=1)
student.delete()
```

---

# 12. Key Features of Python

- Easy to Learn
- Simple Syntax
- High-Level Language
- Interpreted Language
- Object-Oriented
- Open Source
- Portable
- Large Standard Library
- Dynamically Typed
- Extensive Community Support

---

# 📌 Summary

Today I learned:

- Introduction to Python
- Python Basics
- Comments
- Applications of Python
- Advantages & Disadvantages
- Django Framework
- MVT Architecture
- MVT Workflow
- Django ORM
- CRUD Operations
- Features of Python

---

## 🚀 Next Topics

- Variables
- Data Types
- Operators
- Input & Output
