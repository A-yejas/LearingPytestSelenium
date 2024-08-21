'''
What Is Inheritance?
The method of inheriting the properties of parent class into a child class is known as inheritance. It is an OOP concept.
Following are the benefits of inheritance.

**Code reusability- we do not have to write the same code again and again, we can just inherit the properties we need in a child class.

**It represents a real world relationship between parent class and child class.

**It is transitive in nature. If a child class inherits properties from a parent class, then all other sub-classes of the child class
will also inherit the properties of the parent class.

Types:
Single level
Multiple
Multilevel
Optional: Hierarchical
'''


class Parent():
    def first(self):
        print('first function: Manju')
    def firsts(self):
        print("Salman")


class Child(Parent):
    def second(self):
        print('second function')


ob = Child()
ob.first()
ob.second()




# Using inheritance we can get parent class properties into child class

# class Mat_Oper():
#     name = 'sriram'      # Class variable
#     def add(self, a, b):
#         print('sum is', a + b)
#
#     def sub(self, a, b):
#         print('sub is', a - b)
#
# class Number_Oper(Mat_Oper):
#     pass
#
#
# inst = Number_Oper()
# print(dir(inst))
# inst.add(3,5)
# print(inst.name)

