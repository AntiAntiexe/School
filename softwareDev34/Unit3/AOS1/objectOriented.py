#create a class and creat an instance(object p1) of a class (newClass) and print x
class newClass:
    x = 5

p1 = newClass()
p2 = newClass()
p3 = newClass()
print(p1.x)
print(p2.x)
print(p3.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()