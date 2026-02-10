class Person:
 def __init__(self, name, age):
   self.name = name
   self.age = age
 def __str__(self):
    return f"{self.name} is {self.age} years old."

p1 = Person("Alice", 30)
print(p1)