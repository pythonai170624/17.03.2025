'''
1. What is Object-Oriented Programming (OOP)?
   Class and object
   Encapsulation
   Inheritance
   Polymorphism
   Abstract
2. What is the difference between __init__ and __new__ in Python?
3. What is inheritance in Python?
4. Explain method overriding
5. What is the difference between class variables and instance variables?
6. What are decorators in Python?  How are they used in OOP?
   @property @setter @override @staticmethod @abstract @final @classmethod
7. What is encapsulation in Python? How is it implemented?
9. What are magic methods or dunder methods in Python?
10. What is the super() function used for in Python
class A:
  def __init__(self, x, y=5):
    self.x = x
    self.y = y
class B(A):
  def __init__(self, z, x):
    super().__init__()

x = Obj()
y = x

11. What is a metaclass in Python?
  *discuss after test
  class MyMeta(type):  # Inheriting from `type` makes it a metaclass
    def __init__(cls, name, bases, class_dict):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, class_dict)
  class MyClass1(Item, metaclass=MyMeta):  # Using MyMeta as a metaclass
    pass
  class MyClass2(Character, metaclass=MyMeta):  # Using MyMeta as a metaclass
    pass
12. What are abstract base classes in Python?
13. What is the difference between @staticmethod and @classmethod?
17. How does garbage collection work in Python?
18. What is multiple inheritance in Python? (interface + class)
'''