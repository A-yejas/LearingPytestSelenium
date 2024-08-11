# Single Inheritance :- When a child class inherits only a single parent class.

class Parent:
     def func1(self):
          print("this is function one")
class Child(Parent):
     def func2(self):
          print(" this is function 2 ")
ob = Child()
ob.func1()
ob.func2()