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
print(">>>>>>>")
class Parent:
    def greet(self):
        print("Hello from the Parent class!")

class Child(Parent):
    def greet(self):
        print("Hello from the Child class!")
        super().greet()  # Calls the greet method from the Parent class


child = Child()
child.greet()


